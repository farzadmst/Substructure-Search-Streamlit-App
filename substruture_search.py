import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import PandasTools
import pandas as pd
st.image("SubStruture_Search.png",use_container_width=True)

#st.title("Substructure Search in SMILES Dataset",)

#Uploading the CSV file
uploaded_file = st.file_uploader("Upload a CSV file containing SMILES", type=["csv"])
if uploaded_file:
    smiles_data = pd.read_csv(uploaded_file)
    st.write("Dataset Loaded Successfully!")
    st.dataframe(smiles_data.head(10))
    
    #Select the SMILES column
    smiles_col = st.selectbox("Select the column containing SMILES:", smiles_data.columns)
    
    # Substructure Input
    substructure = st.text_input("Enter the Substructure:")
    if substructure:
        try:
            query = Chem.MolFromSmarts(substructure)
            if query is None:
                st.error("Invalid SMARTS pattern.")
            else:
                # Substructure search in dataset
                matches = []
                for idx, row in smiles_data.iterrows():
                    mol = Chem.MolFromSmiles(row[smiles_col])
                    if mol and mol.HasSubstructMatch(query):
                        matches.append(row)
                
                # Showing the result
                if matches:
                    results_df = pd.DataFrame(matches)
                    st.write("{} of the structures have the substructure!".format(len(matches)))
                    st.dataframe(results_df)
                    
                    # Render match molecules
                    mols = [Chem.MolFromSmiles(row[smiles_col]) for row in matches]
                    img = Draw.MolsToGridImage(mols, molsPerRow=4, subImgSize=(200, 200))
                    st.image(img)
                else:
                    st.write("No matches found.")
        except Exception as e:
            st.error(f"Error: {str(e)}")