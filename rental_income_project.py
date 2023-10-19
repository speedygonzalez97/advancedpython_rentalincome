class Roi():

    def __init__(self,income,expenses,cashflow,cashOncash):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.cashOncash = cashOncash
        self.total_income =  0
        self.total_expenses = 0
        self.total_total_investment = 0
        self.total_annual_cash_flow = 0

    def calcIncome(self):
       
        r_i = int(input("\nWhat is your rental income? "))
        self.income.append(r_i)
        
        l_i = int(input("What is your laundry income? "))
        self.income.append(l_i)

        s_i = int(input("What is your storage income? "))
        self.income.append(s_i)

        o_i = int(input("What is your other income? "))
        self.income.append(o_i)

        total = 0
        for income in range(0, len(self.income)):
            total = total + self.income[income]
        
        self.total_income = total

        print(f"\nYour total income is ${self.total_income}.\n")
            

    def calcExpenses(self):
        
        t_e = int(input("What is your tax expenses? "))
        self.expenses.append(t_e)

        i_e = int(input("What is your insurance expenses? "))
        self.expenses.append(i_e)

        u_e = int(input("What is your utility expenses? "))
        self.expenses.append(u_e)

        hoa_e = int(input("What is your HOA expenses? "))
        self.expenses.append(hoa_e)

        l_e = int(input("What is your lawn/snow expenses? "))
        self.expenses.append(l_e)

        v_e = int(input("What is your vacancy expenses? "))
        self.expenses.append(v_e)

        r_e = int(input("What is your repairs expenses? "))
        self.expenses.append(r_e)

        c_e = int(input("What is your capital expenditure expenses? "))
        self.expenses.append(c_e)

        p_e = int(input("What is your property manage expenses? "))
        self.expenses.append(p_e)

        m_e = int(input("What is your mortgage expenses? "))
        self.expenses.append(m_e)

        total = 0
        for expenses in range(0, len(self.expenses)):
            total = total + self.expenses[expenses]
        
        self.total_expenses = total

        print(f"\nYour total expenses is ${self.total_expenses}.")

    def calcCashflow(self):

        total_monthly_cash_flow = self.total_income - self.total_expenses
        print(f"\nYour total monthly cash on cash flow is ${total_monthly_cash_flow}.")

        self.total_annual_cash_flow = total_monthly_cash_flow * 12
        print(f"\nYour total annual cash on cash flow is ${self.total_annual_cash_flow}.\n")

    def calcCashonCash(self):

        dp = int(input("What is your down payment? "))
        self.cashOncash.append(dp)

        cc = int(input("What is your closing costs? "))
        self.cashOncash.append(cc)

        rb = int(input("What is your rehab budget? "))
        self.cashOncash.append(rb)

        oi = int(input("What is your other investments? "))
        self.cashOncash.append(oi)

        total = 0
        for investment in range(0, len(self.cashOncash)):
            total = total + self.cashOncash[investment]
        
        self.total_total_investment = total

        print(f"\nYour total investment is ${self.total_total_investment}.")

        return_on_investment = (self.total_annual_cash_flow / self.total_total_investment) * 100

        print(f"\nYour Return on Investment(ROI) is {return_on_investment}%\n.")


calcRoi = Roi([],[],0,[])


calcRoi.calcIncome()

calcRoi.calcExpenses()

calcRoi.calcCashflow()

calcRoi.calcCashonCash()

