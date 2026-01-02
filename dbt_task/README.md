Welcome to your new dbt project!

### Process followed in this project.

1. Created staging folder and placed users,orders,events sql files and run command dbt run --select staging.
2. Created transformations folder and placed first_click, last_click sql files and run command dbt run --select clicks_transformations.
3. In both the folders schema.yml files are created and run dbt test to null tests.
4. Now to create a dashboard i exported csv files of first_click and second_click output data using export_op.py.
5. Created a dashboard using dashboard.py.

