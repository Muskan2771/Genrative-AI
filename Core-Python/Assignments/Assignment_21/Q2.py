class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def get_data(self):
        try:
            self.model_number = int(input("Enter Model Number: "))
            if len(str(self.model_number)) > 4:
                raise ValueError("Model number must be at most 4 digits")

            self.screen_size = int(input("Enter Screen Size (in inches): "))
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches")

            self.price = float(input("Enter Price: "))
            if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0 and 5000 Rs")

        except Exception as e:
            print("Exception caught:", e)
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\n--- Television Details ---")
        print("Model Number:", self.model_number)
        print("Screen Size :", self.screen_size)
        print("Price       :", self.price)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    tv = Television()
    tv.get_data()
    tv.display()
