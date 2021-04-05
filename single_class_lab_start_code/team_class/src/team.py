class Team:

    def __init__(self, name: str, players: list, coach: str):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player: str):
        self.players.append(new_player)
    
    def has_player(self, player: str):
        if player in self.players:
            return True
        return False
    
    def play_game(self, result):
        if result == True:
            self.points += 3
        