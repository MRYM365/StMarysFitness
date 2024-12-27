class PaymentView:
    @staticmethod
    def display_subscription_details(subscription):
        print(f"Subscription ID: {subscription.subscription_id}")
        print(f"Member: {subscription.member.name}")
        print(f"Plan: {subscription.plan}")
        print(f"Fee: ${subscription.fee}")
        print(f"Discount: {subscription.discount}%")
        print(f"Final Fee: ${subscription.calculate_final_fee()}")
        print(f"Status: {subscription.status}")

    @staticmethod
    def display_payment_details(payment):
        print(f"Payment ID: {payment.payment_id}")
        print(f"Subscription: {payment.subscription.subscription_id}")
        print(f"Amount: ${payment.amount}")
        print(f"Payment Date: {payment.payment_date}")
        print(f"Payment Method: {payment.payment_method}")

    @staticmethod
    def get_subscription_input():
        plan = input("Enter Subscription Plan (Monthly/Quarterly/Annual): ")
        fee = float(input("Enter Subscription Fee: "))
        discount = float(input("Enter Discount (0 if none): "))
        return plan, fee, discount

    @staticmethod
    def get_payment_input():
        subscription_id = input("Enter Subscription ID: ")
        amount = float(input("Enter Payment Amount: "))
        payment_method = input("Enter Payment Method (Credit Card/Cash): ")
        return subscription_id, amount, payment_method
