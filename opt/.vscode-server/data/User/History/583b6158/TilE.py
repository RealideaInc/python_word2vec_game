from gensim.models import KeyedVectors
import random

def exist_word_in_model(model, word):
    return word in model.index_to_key

def player_input_word(model, player_name):
    while(1): 
        word = input('{}さんの入力です: '.format(player_name))
        if word in model.index_to_key:
            print('入力を受け付けました。{}さんの入力「{}」\n'.format(player_name, word))
            return word
        elif '[{}]'.format(word) in model.index_to_key:
            print('入力を受け付けました。{}さんの入力「{}」\n'.format(player_name, word))
            return '[{}]'.format(word)
        else:
            print('存在しない単語です。入力し直してください。\n')

def print_title(title, description):
    u = '┌──  {}  '.format(title) + '─'*(len(description)-len(title)-1)*2 + '┐'
    m = '|  ' + description + '  |'
    b = '└' + '─'*(len(m)-4)*2 + '┘'
    print(u,m,b, sep='\n')

def title_image():
    print('\n\n')
    print('【Python】近い・遠い言葉当てゲーム')
    print('**********************')
    print('* 1.  遠い言葉ゲーム *')
    print('* 2.  近い言葉ゲーム *')
    print('* 3.  終了　　　　　 *')
    print('**********************')
    while(1):
        num = input('番号を選択してください\n')
        if num.isdigit():
            return int(num)
        else:
            print('有効なキーを入力してください')

def close_words_game():
    while(1):
        random_word = random.choice(model.index_to_key)
        print('\n\nお題：「{}」に近い言葉'.format(random_word))
        ok = input('''---
選び直す場合は「n」を押してEnterキーを押してください。このお題で良い場合は、Enterを押してください。
Enter: OK!!
n: 選び直す
---
''')
        if ok != 'n':
            break

    print_title("「{}」に近い単語は？".format(random_word))

    p1_word = player_input_word(model, 'player1')
    p2_word = player_input_word(model, 'player2')

    similarity1 = int((model.similarity(random_word, p1_word)+2)*1000)
    similarity2 = int((model.similarity(random_word, p2_word)+2)*1000)
    print('Player1: {}点 ({})'.format(similarity1, p1_word))
    print('Player2: {}点 ({})\n'.format(similarity2, p2_word))

    if similarity1 > similarity2:
        print('「Player1」の勝利！')
    elif similarity1 < similarity2:
        print('「Player2」の勝利！')
    else:
        print('引き分け')

    input('--- Enterで終了 ---')

def far_words_game():
    while(1):
        random_word = random.choice(model.index_to_key)
        print('\n\nお題：「{}」から遠い言葉'.format(random_word))
        ok = input('''選び直す場合は「n」を押してEnterキーを押してください。このお題で良い場合は、Enterを押してください。
Enter: OK!!
n: 選び直す

''')
        if ok != 'n':
            break

    print("「{}」から遠い単語は？".format(random_word))

    p1_word = player_input_word(model, 'player1')
    p2_word = player_input_word(model, 'player2')

    similarity1 = int((model.similarity(random_word, p1_word)+2)*1000)
    similarity2 = int((model.similarity(random_word, p2_word)+2)*1000)
    print('Player1: {}点 ({})'.format(similarity1, p1_word))
    print('Player2: {}点 ({})\n'.format(similarity2, p2_word))

    if similarity1 > similarity2:
        print('「Player2」の勝利！')
    elif similarity1 < similarity2:
        print('「Player1」の勝利！')
    else:
        print('引き分け')
    
    input('--- Enterで終了 ---')

if __name__=='__main__':
    print('読み込み中…')
    model_dir = '../entity_vector/entity_vector.model.bin'
    model = KeyedVectors.load_word2vec_format(model_dir, binary=True)

    while(1):
        q_num = title_image()
        if q_num == 1:
            far_words_game()
        elif q_num == 2:
            close_words_game()
        elif q_num == 3:
            print('Bye!!')
            exit()
