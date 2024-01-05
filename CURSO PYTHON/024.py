import emoji
cidade = str(input('Digite o nome de uma cidade: ')).strip()
cid= cidade.capitalize()
cidade2 = cid.split()
if cidade2[0] == 'Santo':
    print(emoji.emojize('Pelo que vi, o nome da sua cidade começa com SANTO :grinning_face_with_big_eyes: :thumbs_up:'))
else:
    print(emoji.emojize('Pelo que vi, o nome da sua cidade não começa com SANTO :fearful_face:',language='alias'))

