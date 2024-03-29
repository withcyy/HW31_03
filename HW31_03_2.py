class MetricConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084

    @staticmethod
    def get_conversion_count():
        return 2

meters_value = 10
feet_value = MetricConverter.meters_to_feet(meters_value)
print(f"{meters_value} M = {feet_value} F")

feet_value = 30
meters_value = MetricConverter.feet_to_meters(feet_value)
print(f"{feet_value} F = {meters_value} M")

print("Counts: ", MetricConverter.get_conversion_count())