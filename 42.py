'''
Задача 42 Узнать какая максимальная households в зоне минимального значения population.
'''

df[df['population'] < df['population'].quantile(.25)]['households'].max()
подробности:
df['population'].quantile(.25)
df['population'] < df['population'].quantile(.25)
df['population'] < df['population'].quantile(.25)]['households']
