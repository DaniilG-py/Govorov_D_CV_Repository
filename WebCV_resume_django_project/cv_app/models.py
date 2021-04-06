from django.db import models



class WorkingExperience(models.Model):
    """
    Информация об опыте работы
    """

    company_name = models.CharField(max_length=255, verbose_name='Место работы')
    position = models.CharField(max_length=300, verbose_name='Должность')
    start_date = models.DateField(verbose_name='Начало работы')
    end_date = models.DateField(
            verbose_name='Окончание работы',
            null=True,
            blank=True,
            help_text='Оставьте поле пустым чтобы получить значение "По настоящее время"',
        )
    responsibilities = models.TextField(verbose_name='Описание обязанностей')
    company_web_address = models.CharField(max_length=100, verbose_name='Сайт компании', null=True, blank=True)

    def __str__(self):
        return f'{self.position} - {self.company_name}'

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'
        ordering = ['-start_date']


class EducationExperience(models.Model):
    """
    Информация об обучении
    """
    GRAD_YEARS = (
            '2013',
            '2014',
            '2015',
            '2016',
            '2017',
            '2018',
            '2019',
            '2020',
            '2021',
        )
    HIGHER_EDUCATION = 'Высшее образование'
    COURSE = 'Курсы'

    GRAD_YEAR_CHOICE = (
            (GRAD_YEARS[0], '2013'),
            (GRAD_YEARS[1], '2014'),
            (GRAD_YEARS[2], '2015'),
            (GRAD_YEARS[3], '2016'),
            (GRAD_YEARS[4], '2017'),
            (GRAD_YEARS[5], '2018'),
            (GRAD_YEARS[6], '2019'),
            (GRAD_YEARS[7], '2020'),
            (GRAD_YEARS[8], '2021'),
        )

    CATEGORY_CHOICE = (
            (HIGHER_EDUCATION, 'Высшее образование'),
            (COURSE, 'Повышение квалификации, курсы'),
        )

    grad_year = models.CharField(max_length=4, choices=GRAD_YEAR_CHOICE, verbose_name='Год окончания')
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICE, verbose_name='Тип обучения')
    place = models.CharField(max_length=255, verbose_name="Место обучения")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        ordering = ['-grad_year']

    def __str__(self):
        return self.place
