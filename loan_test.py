def test_Gender():
    assert df['Gender'].unique().tolist()==['male','Female']

def test_Married():
    assert df["Married"].unique().tolist()==['Yes','No']

def test_ApplicantIncome():
    assert df[df['ApplicantIncome'] <0].shape[0] ==0
def test_LoanAmount():
    assert df[df['Loan_Amount_Term']> 600].shape[0] ==0


