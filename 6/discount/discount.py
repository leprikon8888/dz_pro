class Discount:
    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def discount(self):
        return 0.01


class SilverDiscount(Discount):
    def discount(self):
        return 0.05


class GoldDiscount(Discount):
    def discount(self):
        return 0.1


class PlatinumDiscount(Discount):
    def discount(self):
        return 0.15

