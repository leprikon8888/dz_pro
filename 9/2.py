'''Створіть абстрактний базовий клас "ПлатіжнийЗасіб" з методом "здійснити_платіж()". Створіть підкласи "КредитнаКарта",
"БанківськийПереказ", "ЕлектроннийГаманець" і т.д., які успадковують цей метод та реалізовують його відповідно до
специфіки кожного платіжного засобу. Створіть клас "ПлатіжнийПроцесор", який містить список доступних платіжних засобів
та метод для виконання платежу через вибраний засіб. Можна створити об'єкти різних платіжних засобів, додати їх до
платіжного процесора і здійснити платежі через них'''


class PaymentInstrument:

    def make_a_payment(self):
        raise NotImplementedError('нужно реализовать')


class CreditCart(PaymentInstrument):
    def make_a_payment(self):
        return 'payment by credit card'


class BankTransfer(PaymentInstrument):
    def make_a_payment(self):
        return 'payment by bank transfer'


class ElectronicWallet(PaymentInstrument):
    def make_a_payment(self):
        return 'payment by electronic money'


class PayProcessor:

    def __init__(self):
        self.list_instruments = []

    def add_instrument(self, instrument: PaymentInstrument):
        if not isinstance(instrument, PaymentInstrument):
            raise TypeError('ожидаем другой тип данных')
        elif not instrument in self.list_instruments:
            self.list_instruments.append(instrument)
        else:
            raise Exception("этот платежный метод уже есть в списке")

    def run_pay(self, instrument: PaymentInstrument):
        if instrument in self.list_instruments:
            print(instrument.make_a_payment())
        else:
            raise ValueError('Pay error, pay instument is not defined')


if __name__ == "__main__":

    cred = CreditCart()
    bank = BankTransfer()
    e_wallet = ElectronicWallet()

    proc = PayProcessor()

    proc.add_instrument(cred)
    proc.add_instrument(bank)
    proc.add_instrument(e_wallet)

    proc.run_pay(cred)
    proc.run_pay(bank)
