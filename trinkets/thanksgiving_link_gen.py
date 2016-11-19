from random import choice

t_words = [ 'pie', 'autumn', 'baste', 'colonists', 'cornucopia',
            'cranberry', 'drumstick', 'fall', 'giblets', 'gobble',
            'gravy', 'ham', 'indian', 'leaves', 'massachusetts',
            'mayflower', 'massasoit', 'melting', 'pot', 'native',
            'american', 'november', 'patuxet', 'pilgrim', 'plymouth',
            'rock', 'pumpkin', 'sauce', 'settlers', 'squanto',
            'squash', 'stuffing', 'corn', 'potato', 'sweet', 'thanksgiving',
            'tisquantum', 'turkey', 'voyage', 'wampanoag', 'wishbone', 'yam'
]

def thanksgivingLinkGen():

    separator = '-'
    numlength = 4
    nums='0123456789'
    word1 = choice(t_words)
    word2 = choice(t_words)
    newNum = ''.join(choice(nums) for i in range(numlength))
    frags = [word1, word2, newNum]
    return separator.join(frags)
