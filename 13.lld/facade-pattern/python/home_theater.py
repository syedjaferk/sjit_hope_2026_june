# Subsystem classes
class Amplifier:
    def turn_on(self):
        print("Amplifier turned on")

    def turn_off(self):
        print("Amplifier turned off")


class DVDPlayer:
    def play_movie(self, movie):
        print(f"Playing movie: {movie}")

    def stop_movie(self):
        print("Stopping movie")


class Projector:
    def turn_on(self):
        print("Projector turned on")

    def turn_off(self):
        print("Projector turned off")


class Lights:
    def dim_lights(self):
        print("Dimming lights")

    def brighten_lights(self):
        print("Brightening lights")


# Facade class
class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, projector, lights):
        self.amplifier = amplifier
        self.dvd_player = dvd_player
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie!")
        self.lights.dim_lights()
        self.amplifier.turn_on()
        self.projector.turn_on()
        self.dvd_player.play_movie(movie)

    def end_movie(self):
        print("Movie night is over!")
        self.dvd_player.stop_movie()
        self.amplifier.turn_off()
        self.projector.turn_off()
        self.lights.brighten_lights()


# Client code
amplifier = Amplifier()
dvd_player = DVDPlayer()
projector = Projector()
lights = Lights()

home_theater = HomeTheaterFacade(amplifier, dvd_player, projector, lights)

# Watching a movie using the Facade
home_theater.watch_movie("Inception")

# Ending the movie night
home_theater.end_movie()
