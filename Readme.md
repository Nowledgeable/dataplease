# Dataplease

Let you generate fake data as pandas dataframe or sql dump easily 
Useful for big data projects for instance

## installation 

1. For now : download the files or git clone
2. run `pip install numpy pandas`

## usage

### Generate dataset using ready to use dataset generator 

We provide two ready-to use generator so far 
- A house dataset (house_generator.py)
- A banking transaction dataset (transaction_generator.py)

Choose how many rows you generate :


1. Open the file you want to use
2. Edit the row using the function "generate_df". The first argument is the number of row 
3. launch `python nameofthefile` 

Example : 
```bash
python house_generator.py
```

## Licence MIT 
