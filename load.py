from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine(
        "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/credit_risk_db"
    )

    print("Loading dim_customer...")

    dim_customer = df[[
        "SK_ID_CURR",
        "CODE_GENDER",
        "NAME_EDUCATION_TYPE",
        "NAME_FAMILY_STATUS",
        "NAME_INCOME_TYPE",
        "age"
    ]].drop_duplicates()

    dim_customer.columns = [
        "customer_id",
        "gender",
        "education_type",
        "family_status",
        "employment_type",
        "age"
    ]

    dim_customer.to_sql("dim_customer", engine, if_exists="append", index=False)

    print("Loading fact_loans...")

    fact_loans = df[[
        "SK_ID_CURR",
        "AMT_CREDIT",
        "AMT_ANNUITY",
        "AMT_GOODS_PRICE",
        "TARGET"
    ]]

    fact_loans.columns = [
        "customer_id",
        "credit_amount",
        "annuity_amount",
        "goods_price",
        "default_flag"
    ]

    fact_loans.to_sql("fact_loans", engine, if_exists="append", index=False)

    print("Load completed.")
