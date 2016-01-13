'''
Name: Spencer Klinge
Date: 10/08/15
Class: ISTA 130
Section Leader: Will

Description:
This program builds a simple dice game called “Pig”.
In this version of Pig, two players will alternate turns. Players each begin
the game with a score of 0. During a turn a player will roll a six-sided die one
or more times, summing up the resulting rolls. At the end of the player’s turn
the sum for that turn is added to the player’s total game score.
If at any time a player rolls a 1, the player’s turn immediately ends and
he/she earns 0 points for that turn (i.e. nothing is added to the player’s total
game score). After every roll the player may choose to either end the turn,
adding the sum from the current turn to his/her total game score, or roll again
in an attempt to increase the sum.
The first player to 50 points wins the game.
'''
import random
def print_scores(name1,score1,name2,score2):
    '''
    This function prints the names and scores of the two
    players in the format outlined by the instructions    
    Parameters:
    name1: string, player 1 name
    score1: int, player 1 score
    name2: string, player 2 name
    score2: int, player 2 score
    Returns: None
    '''
    print ('\n--- SCORES\t'+name1+':',str(score1)+'\t'+name2+':',str(score2),'---')

def check_for_winner(name, score):
    '''
    This function Checks to see if the givin player has reached 50,
    thus winning the game
    
    Parameters:
    name: player name being checked,
    score: player score being checked.
    Returns: Boolean
    '''
    if score >= 50:
        print('THE WINNER IS:',name+"!!!!!")
        return True
    return False

def roll_again(player_name):
    '''
    This function takes user input to check and see if the player wants to 
    take another chance in their turn to add to their score.
    
    Parameters:
    player_name: string, player whose turn it is
    Returns: Boolean
    '''
    again= True
    while(again):
        answer= input('Roll again, '+player_name+'? (Y/N) ')
        if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
            again= False
        else:
            print("I don't understand:",'"'+answer+'".', 'Please enter either '+'"'+'Y'+'"'+' or '+'"'+'N'+'".')
    if answer=='Y' or answer=='y':
        return True
    if answer=='N' or answer== 'n':
        return False

def play_turn(players_name):
    '''
    This function goes through the phases of a single turn and loop sums a temp score
    until a one is rolled or the player opts out of another roll. if the player rolls a one,
    they lose all the points they gained from that turn. if they opt out before they roll a 
    one, the points are added to their total
    
    Parameters:
    player_name: string, player whose turn it is
    Returns: Boolean
    '''
    temp_score=0
    print('----------', players_name+"'s", 'turn ----------')
    boolin= True
    while(boolin):
        rand_int= random.randint(1,6)
        print('\t'+'<<<',players_name, 'rolls a', str(rand_int),'>>>')
        if rand_int ==1:
            temp_score=0
            print('\t'+'!!! PIG!','No points earned, sorry', players_name,'!!!')
            boolin= False
            input('(enter to continue)')
        else:
            temp_score+=rand_int
            print('\t'+'Points:',temp_score)
            if not roll_again(players_name):
                boolin= False
    return temp_score



def main():
    '''
    main sets up the game and handels the checking for a winner. it sets up the random 
    seed and takes the player names.
    '''
    seed= input("Enter seed value:")
    random.seed(seed)
    print()
    print()
    print("Pig Dice")
    player1= input('Enter name for player 1: ')
    player2= input('Enter name for player 2: ')
    print('\t'+'Hello',player1,'and',player2+',','welcome to Pig Dice!')
    score1=0
    score2=0
    print_scores(player1, score1, player2, score2)
    booling=True
    while(booling):
        score1= score1 + play_turn(player1)
        print_scores(player1, score1, player2, score2)
        if(not check_for_winner(player1, score1)):
            score2= score2 + play_turn(player2)
            print_scores(player1, score1, player2, score2)
        else:
            booling=False
            continue
        if(check_for_winner(player2, score2)):
            booling=False
    input('(enter to continue)')

if __name__ == '__main__':
    main()
