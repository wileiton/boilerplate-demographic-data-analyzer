import pandas as pd

def calculate_demographic_data(print_data=True):

    # Leer datos
    df = pd.read_csv("adult.data.csv")

    # Número de cada raza
    race_count = df['race'].value_counts()

    # Edad promedio de hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentaje con Bachelor's
    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100,
        1
    )

    # Educación avanzada
    higher_education = df['education'].isin([
        'Bachelors',
        'Masters',
        'Doctorate'
    ])

    # Sin educación avanzada
    lower_education = ~higher_education

    # Porcentaje ricos con educación avanzada
    higher_education_rich = round(
        (
            df[higher_education & (df['salary'] == '>50K')].shape[0]
            / df[higher_education].shape[0]
        ) * 100,
        1
    )

    # Porcentaje ricos sin educación avanzada
    lower_education_rich = round(
        (
            df[lower_education & (df['salary'] == '>50K')].shape[0]
            / df[lower_education].shape[0]
        ) * 100,
        1
    )

    # Horas mínimas de trabajo
    min_work_hours = df['hours-per-week'].min()

    # Personas que trabajan mínimo de horas
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Porcentaje ricos entre los que trabajan menos horas
    rich_percentage = round(
        (
            num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]
            / num_min_workers.shape[0]
        ) * 100,
        1
    )

    # País con mayor porcentaje de ricos
    country_rich = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts()
        / df['native-country'].value_counts()
        * 100
    )

    highest_earning_country = country_rich.idxmax()

    highest_earning_country_percentage = round(
        country_rich.max(),
        1
    )

    # Ocupación más popular en India para >50K
    top_IN_occupation = (
        df[
            (df['native-country'] == 'India') &
            (df['salary'] == '>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    # Mostrar resultados
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }