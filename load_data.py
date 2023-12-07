
import psycopg2
from psycopg2.extras import execute_values
from read_data import return_std_data

if __name__ == "__main__":

    # I pulled a quick postgres image
    datasets = return_std_data()

    connection = psycopg2.connect(host='localhost',
                              user='postgresUser',
                              password='postgresPW', 
                              dbname='postgres',
                              port='5455')


    with connection as conn:
        with connection.cursor() as cur:
            
            for dataset in datasets:
                # skipping texas on purpose
                if dataset == []:
                    continue
                columns = dataset[0].keys()
                query = "INSERT INTO assessment ({}) VALUES %s".format(','.join(columns))


                values = [[value for value in row.values()] for row in dataset]
                execute_values(cur, query, values)
                conn.commit()
        print("done")