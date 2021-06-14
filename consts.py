from random import randint


salaries = {
    '0-50': randint(0, 50) * 1000,
    '50-100': randint(50, 100) * 1000,
    '100-130': randint(100, 130) * 1000,
    '130-160': randint(130, 160) * 1000,
    'Больше 160': randint(160, 200) * 1000,
    'Ничего вам не скажу': 100000,
}

PERFECT_KBD_LAYOUT = [['Git'], ['SQL'], ['Python'], ['Data Analysis'], ['Перейти к выбору навыков, которые хочется подтянуть']]
MIDDLE_KBD_LAYOUT = [['Web'], ['Algorithms'], ['ML'], ['Docker'], ['Перейти к выбору навыков, которые хочется изучить']]
WEAK_KBD_LAYOUT = [['CI/CD'], ['Testing'], ['Golang'], ['Asyncio'], ['Перейти к рекомендациям']]
