# IoT for Plants

A Node.js + Express web application that embeds a Power BI report and displays data metrics read from a RaspberryPi to determine optimal conditions for house plants. 

### Raspberry pi SenseHat sensors used 
- Temperature
- Humidity
- Pressure
- Orientation (jaw)

### Power BI Embedded Report
- Secure embedding using Power BI's embed URL  
- Styled dashboard page with navbar, title, and descriptive text  
- Responsive iframe layout  

### CSV Data Viewer
- Reads the csv with the sensor data  
- Displays it in a styled HTML table  

## Technologies and libraries

- **Raspberrypi**
- **SenseHat** 
- **Node.js**  
- **Express.js**  
- **EJS** templating  
- **csv-parser** for CSV ingestion  
- **Power BI Embedded (iframe)**  
- **HTML/CSS** for layout and styling  
