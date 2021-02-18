class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calculation(self, asphalt_mass, height):
        return (self._length * self._width * asphalt_mass * height)/1000


rural_highway = Road(5000, 20)
print(f"понадобится {int(rural_highway.asphalt_mass_calculation(25, 5))} т. асфальта, "
      f"чтобы покрыть всё дорожное полотно.")
