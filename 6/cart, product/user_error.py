class CartLimitError(Exception):
    def __init__(self, max_el, message='too many carts'):
        self.message = message
        self.max_el = max_el
        super().__init__(self.message)

    def __str__(self):
        return f'Limit of carts {self.max_el} \n  {self.message}'


