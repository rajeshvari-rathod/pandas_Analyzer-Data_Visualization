import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

class SalesDataAnalyzer:

    def __init__(self):
      self.data = None
      self.graph = None

    def load_dataset(self):
        try:
            print("*********************************")
            print("********** Load dataset **********")
            self.data = input("Enter the path of dateset (CSV file)")
            self.data = pd.read_csv(f'{self.data}')
            print("Dataset Load Sucessfully")
            return self.data
            
        except:
            print("Enter your valid data")  

    def explore_data(self):
        try:
            print("********************************")
            print("********** Explore Data **********")
            print("1. Displya the first 5 row") 
            print("2. Displya the last 5 row")
            print("3. Displya column name")      
            print("4. Displya data type")
            print("5. Basic info")
            print()

            choice = int(input("Enter your choice number (1-5)"))
            print()

            if choice == 1:
                head = self.data.head()
                print(head)
                print()

            elif choice == 2:
                tail = self.data.tail()
                print(tail)

            elif choice == 3:
                cols = self.data.columns
                print(cols)

            elif choice == 4:
                dt = self.data.dtypes
                print(dt)

            elif choice == 5:
                info = self.data.info()
                print(info)

            else:
                print("Invalid choice")  
        except:
            print("Enter your valid number")

    def data_frame(self):  
        try:
            pass
        except:
            pass  

    def handal_missingdata(self):
        try:
            print("******************************")
            print("********** Handle Misssing Data *********")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")

            choice = int(input("Enter your number (1-4)"))

            if choice == 1:
               if  self.data.isnull().empty:
                   print("No misssing values found in the dataset")
               else:
                   null = self.data.isnull()
                   print(null)    

            elif choice == 2:
                df = self.data.fillna(self.data.mean())
                print(df.head())

            elif choice == 3:
                print("Before Cleaning")
                print(df.isnull().sum())
                df = self.data.dropna()
                print("After Cleaning")
                print(df.isnull().sum())

            elif choice == 4:
                replace = input("Enter a value missing with replace")
                dt = self.data.fillna(replace)
                print(f"missing value replace {replace} with successfully")

            else:
                print("Invalid choice")
        except:
                print("Enter your valid number")

    def generate_statistics(self):
        try:
            pass
        except:
            pass

    def data_visulization(self):
        try:
           print("******************************")
           print("********** Data Visulization **********")
           print("1. Bar Plot")
           print("2. Line Plot")
           print("3. Scatter Plot")
           print("4. Pie Chart")
           print("5. Histogram")
           print("6. Stack Plot")

           choice = int(input("Enter your number (1-6)"))

           if choice == 1:

                column = input("Enter your column for x-axis (e.g. Product)")
                values = input("Enter numberic column for y-axis (e.g Sales)")

                data=pd.dummy_csv("dummy.csv")
                data.head(5)
                num10 = data.nlargest(5,"Profit")
                num10.set_index("Employee_Name")[['Profit','Sales']].plot(
                    kind="bar",
                    figsize=(10,10),
                    
                )
                print(plt.legend())
                print(plt.title("top 5 youger Employee"))
                print(plt.ylabel("Employee_ID"))
                print(plt.xlabel("Employee_Name"))
                print(plt.xticks(rotation=30))
                print(plt.grid(axis="both",linestyle="-",alpha=0.1))
                print(plt.savefig("barchart.png"))
                print(plt.show())

           elif choice == 2:
               pass

           elif choice == 3:
               pass

           elif choice == 4:
               pass

           elif choice == 5:
               pass

           elif choice == 6:
               pass

           else:
                print("Invalid choice")     
        except:
                print("Enter your valid number")

    def save_visualization(self):
        try:
          if self.data is None:
              print("Load the dataset first")
              return
          
          filename = input("Enter your file name(e.g. employee_chart.png)")

          if not filename.lower().endswith(".png"):
              filename += ".png"

              plt.savefig(filename,bbox_inches = "tight")
              print(f"Visualization saved  as {filename}")
        except:
             print("Enter your valid number")


    def main_menu(self):
        while True:
            print()
            print("*************** Data Analysis & Visualization Program ***************")  
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform Dataframe Operations")     
            print("4. Handal Missing Data")
            print("5. Generat Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print()

            choice = int(input("Enter your choice number (1-8)"))
            

            if choice == 1:
                self.load_dataset()

            elif choice == 2:
                self.explore_data()

            elif choice == 3:
                self.data_frame()

            elif choice == 4:
                self.handal_missingdata()

            elif choice == 5:
                self.generate_statistics()

            elif choice == 6:
                self.data_visulization()

            elif choice == 7:
                self.save_visualization()

            elif choice == 8:
                print("Exiting the program. Goodbye")
                break

            else:
                print("Invalid choice number")

    def __del__(self):
        pass

obj = SalesDataAnalyzer()
obj.main_menu()
    
