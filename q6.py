class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50
    
    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
    
    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
    
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1

tv = TV()
print("Canal atual:", tv.canal)
tv.mudarCanal(10)
print("Novo canal:", tv.canal)
print("Volume:", tv.volume)
tv.aumentarVolume()
print("Volume após aumento:", tv.volume)
