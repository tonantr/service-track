# 🚗 Service Track  

## 📌 Features  
✅ User authentication (admin & regular users)  
✅ Manage cars and their service history  
✅ Export service records  
✅ MySQL database support  

## 🏗 Prerequisites  
- **Python 3.10+**  
- **MySQL** (running on Windows/macOS)  

## 📥 Clone the Repository  
```sh
git clone https://github.com/tonantr/service-track.git
cd service-track

###  Install Dependencies
pip install -r requirements.txt

### ## Packaging the App with PyInstaller
macOS:
pyinstaller --add-data ".env:." --name "service_track" main.py
Windows:
pyinstaller --add-data ".env;." --name "service_track" main.py

## 🚀 Running the Application
macOS:
python3 main.py
Windows:
python main.py