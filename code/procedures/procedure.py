from light_utils import colors

class Procedure:

    def __init__(self):
        # these attributes common to all procedures
        self.color_set = None           # which colors to use
        self.color_ordered = None       # use in order or random?
        self.brightness = None          # 0 -> 1 float, [0.1, 0.5]
        self.blink_time = None          # time in seconds
        self.direction = None
        self.run_time = None            # seconds (overrides num_runs)
        self.num_runs = None            # how many times to do proc
        self.fade = None

    def parseParams(self, params):
        """Read all the data from the input dictionary."""

        # unpack the common attributes
        self.color_set = colors.parseColorSet(params["color_set"])
        self.color_ordered = params["color_ordered"]
        self.brightness = params["brightness"]
        self.blink_time = params["blink_time"]
        self.direction = params["direction"]

        # run time is determined by 1) seconds 2) iterations
        if "run_time" in params:
            self.run_time = params["run_time"]
            self.num_runs = None
        else:
            self.run_time = None
            self.num_runs = params["num_runs"]

        # fade may or may not be implemented for a procedure,
        #  but decode it either way
        self.fade = params["fade"] if "fade" in params else False
