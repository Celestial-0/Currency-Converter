from tkinter import *
from tkinter import ttk, messagebox
import requests


class Converter:

  def __init__(self, master):
    self.master = master
    master.title("Currency Converter")

    # Initialize exchange rates data
    self.exchange_rates = {}

    # Create input fields
    self.create_inputs()

    # Configure column resizing
    self.config_column_resize()

    # Create convert button
    self.create_button()

  def create_inputs(self):
    # Amount
    self.lbl_amt = ttk.Label(self.master, text="Amount:")
    self.lbl_amt.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    self.entry_amt = ttk.Entry(self.master)
    self.entry_amt.grid(row=0, column=1, padx=5, pady=5, sticky="we")

    # Source Currency
    self.lbl_src = ttk.Label(self.master, text="Source Currency:")
    self.lbl_src.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    self.var_src = StringVar()
    self.entry_src = ttk.Combobox(self.master,
                                  textvariable=self.var_src,
                                  state="readonly")
    self.entry_src.grid(row=1, column=1, padx=5, pady=5, sticky="we")
    self.entry_src['values'] = CODES

    # Target Currency
    self.lbl_tgt = ttk.Label(self.master, text="Target Currency:")
    self.lbl_tgt.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    self.var_tgt = StringVar()
    self.entry_tgt = ttk.Combobox(self.master,
                                  textvariable=self.var_tgt,
                                  state="readonly")
    self.entry_tgt.grid(row=2, column=1, padx=5, pady=5, sticky="we")
    self.entry_tgt['values'] = CODES

  def config_column_resize(self):
    # Configure column resizing to make input fields equally expandable
    self.master.grid_columnconfigure(1, weight=1)

  def create_button(self):
    # Create convert button
    self.btn_convert = ttk.Button(self.master,
                                  text="Convert",
                                  command=self.convert)
    self.btn_convert.grid(row=3, columnspan=2, padx=5, pady=5)

  def convert(self):
    try:
      amt = self.entry_amt.get().strip()
      src = self.var_src.get()
      tgt = self.var_tgt.get()

      if not amt or not src or not tgt:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

      amt = float(amt)

      if src == tgt:
        result = f"{amt:.2f} {src} = {amt:.2f} {tgt}"
      else:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{src}")
        response.raise_for_status()  # Raise an error for failed response
        data = response.json()
        rates = data["rates"]
        conv_amt = amt * (rates[tgt] / rates[src])
        rounded_amt = round(conv_amt, 2)
        result = f"{amt:.2f} {src} = {rounded_amt:.2f} {tgt}"

      messagebox.showinfo("Conversion Result", result)

    except ValueError:
      messagebox.showwarning("Warning", "Please enter a valid amount.")
    except requests.RequestException as e:
      messagebox.showerror("Error", f"Failed to fetch rates: {str(e)}")
    except Exception as e:
      messagebox.showerror("Error", str(e))


def main():
  root = Tk()
  app = Converter(root)
  root.mainloop()


if __name__ == "__main__":
  CODES = ['AUD', 'EUR', 'GBP', 'INR', 'JPY', 'USD']
  main()
