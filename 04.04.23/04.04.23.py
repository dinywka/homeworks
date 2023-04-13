#25
import datetime
#1
# import datetime
# gmt_time = datetime.datetime.utcnow()
# local_time = datetime.datetime.now()
#
# print("GMT time:", gmt_time)
# print("Local time:", local_time)

#2
# date1 = datetime.date(2023, 4, 1)
# date2 = datetime.date(2023, 4, 11)
# delta = date2 - date1
# print("Days between dates:", delta.days)

#3
import datetime
# delta1 = datetime.timedelta(days=5, hours=2, minutes=30, seconds=10)
# delta2 = datetime.timedelta(days=3, hours=6, minutes=15, seconds=20)
# total_delta = delta1 + delta2
# print("Days:", total_delta.days)
# print("Hours:", total_delta.seconds // 3600)
# print("Minutes:", (total_delta.seconds % 3600) // 60)
# print("Seconds:", total_delta.seconds % 60)

#26
#1
# emails = ['user1@gmail.com', 'user2@hotmail.com', 'user3@yahoo.com', 'user4@gmail.com']
#
# domains = []
#
# for email in emails:
#     domain = email.split('@')[1]
#     if domain not in domains:
#         domains.append(domain)
#
# print(domains)

#2
# text = "The quick brown fox jumps over the lazy dog"
#
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# words = text.split()
#
# vowel_words = []
#
# for word in words:
#     if word[0].lower() in vowels:
#         vowel_words.append(word)
#
# print(vowel_words)

#3
# text = "apple,banana;cherry orange\nwatermelon"
#
# separators = ',; \n'
#
# words = []
#
# start = 0
#
# for i, char in enumerate(text):
#     if char in separators:
#         word = text[start:i]
#         if word:
#             words.append(word)
#         start = i+1
#
# if start < len(text):
#     word = text[start:]
#     if word:
#         words.append(word)
#
# print(words)

#27
candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"] # список кандидатов
votes = [] 

while True:
    vote = input("Выберите кандидата из списка или введите 'стоп', чтобы закончить голосование: ")
    if vote.lower() == "стоп":
        break
    if vote in candidates:
        votes.append(vote)
    else:
        print("Кандидат не найден в списке.")

winners = []
max_votes = 0
for candidate in candidates:
    votes_count = votes.count(candidate)
    if votes_count > max_votes:
        winners = [candidate]
        max_votes = votes_count
    elif votes_count == max_votes:
        winners.append(candidate)

if len(winners) == 2:
    sorted_winners = sorted(winners, key=len)
    winner = sorted_winners[0]
else:
    winner = winners[0]

print(f"Победитель выборов: {winner}. Количество голосов: {max_votes}.")
