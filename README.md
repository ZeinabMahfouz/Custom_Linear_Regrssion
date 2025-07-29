🧠 Linear Regression from Scratch with Custom Train-Test Split (NumPy)
This project demonstrates how to implement a simple linear regression model from scratch using NumPy, along with a custom train-test split function written in a separate Python script.

The model is trained and tested in a Jupyter Notebook, making it easy to follow the steps, visualize intermediate results, and understand the workflow.

🚀 Features
Custom train_test_split_np() function implemented without scikit-learn

Jupyter Notebook demonstration of linear regression using NumPy

Model training using the Normal Equation

Evaluation using Mean Squared Error (MSE)

Optional shuffling and reproducibility via random_seed

📁 Project Structure
bash
Copy
Edit
.
├── train_test_split.py                 # Custom train_test_split_np() function
├── linear_regression_from_scratch.ipynb  # Jupyter Notebook that uses the function and trains the model
└── README.md                           # Project documentation
📚 How to Use
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Requirements
This project only requires NumPy and Jupyter:

bash
Copy
Edit
pip install numpy notebook
3. Run the Notebook
bash
Copy
Edit
jupyter notebook linear_regression_from_scratch.ipynb
You can walk through each cell to see how the data is generated, split, modeled, and evaluated.

🔧 train_test_split_np Function
Defined in: train_test_split.py

python
Copy
Edit
def train_test_split_np(X, y=None, test_size=0.2, shuffle=True, random_seed=None):
    ...
This custom function mimics the behavior of sklearn.model_selection.train_test_split using pure NumPy.

🧪 Example Output
text
Copy
Edit
Mean Squared Error on test set: 0.8836
✅ Highlights
Educational: Great for understanding linear regression internals

Lightweight: No external ML libraries

Modular: Train-test split is reusable across different projects

📌 Future Ideas
Add visualization of regression results

Support polynomial regression

Include a gradient descent version

Package the function for pip install

