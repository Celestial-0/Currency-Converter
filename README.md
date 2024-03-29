# **💱** Currency Converter

This Python script builds upon the existing simple graphical user interface (GUI) for converting between different currencies, adding new features and enhancing user experience.

## 📦 Dependencies

This project relies on the following libraries:

- `**Tkinter**`: `Tkinter` is Python's de-facto standard GUI (Graphical User Interface) package. It provides a fast and easy way to create GUI applications.
- `**Requests**`: `Requests` is an elegant and simple HTTP library for Python, allowing for easy communication with web servers.

## 🚀 Installation

To get started with the Currency Converter application, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using Git by running the following command:
    
    ```bash
    git clone <https://github.com/Celestial-0/Currency-Converter.git>
    ```
    
2. **Navigate to the Directory**: Change your current directory to the cloned repository:
    
    ```bash
    cd Currency-Converter
    ```
    
3. **Install Dependencies**:  Make sure you have Python installed on your system. Then, install the required **`requests`** library using pip:
    
    ```bash
    pip install requests
    ```
    

## 🖥️ Usage

After installing the dependencies, you can run the Currency Converter application:

1. **Run the Application**: Execute the [currency_converter.py]() file:
    
    ```bash
    python currency_converter.py
    ```
    
2. **Conversion Process**: Once the application is running, enter the amount, select the source and target currencies from the dropdown menus, and click the "Convert" button to view the conversion result.
3. **Internet Connection**: Ensure you have an active internet connection as the application fetches the latest exchange rates from an API.

By following these steps, you can easily install and use the Currency Converter application on your local machine.

## 📝 Description

The script now creates an enhanced GUI where users can not only convert currencies but also view historical exchange rate trends. The currency codes available remain 'AUD', 'EUR', 'GBP', 'INR', 'JPY', and 'USD'.

We've added a "Show History" button that fetches historical exchange rates of the past 30 days from the `exchangerate-api` and displays a line graph using matplotlib.

The input validation has also been improved. Now, if the input fields are not properly filled, a user-friendly pop-up message will appear to guide the user.

## 🛠️ Functionality

- `__init__(self, master)`: This function initializes a new instance of the `Converter` class. It sets the window title, initializes exchange rates data, creates input fields, configures column resizing, and creates a convert button.
- `create_inputs(self)`: This function creates input fields for the amount and source/target currencies. It also sets the available currency options.
- `config_column_resize(self)`: This function configures column resizing to make input fields equally expandable.
- `create_button(self)`: This function creates a convert button, which triggers the `convert` function when clicked.
- `convert(self)`: This function handles the conversion process. It first validates the inputs. If the inputs are valid, it fetches the current exchange rates from `exchangerate-api`, performs the conversion, and displays the result in a pop-up message box.
- `main()`: This is the main function that creates a new instance of the Tkinter window and starts the application. It sets the available currency codes and starts the main event loop.

## 📝 Example

<p align="center">
  <img src="https://github.com/Celestial-0/Currency-Converter/raw/main/asset/1.png" alt="Example1"> <img src="https://github.com/Celestial-0/Currency-Converter/raw/main/asset/2.png" alt="Example2">
    
  <img src="https://github.com/Celestial-0/Currency-Converter/raw/main/asset/3.png" alt="Example3">
</p>


## **🤝 Contributing**

We welcome your contributions! Feel free to fork this repository and submit pull requests to make  Currency Converter even better.

## **🌟 Additional Features to Explore**

- Customizable Themes 🎨
- Offline Mode 📴
- Currency Symbols 💱
- Historical Exchange Rates 📈
- Multi-Language Support 🌐
- Enhanced Error Handling ⚠️
