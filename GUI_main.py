import wx
from ATM_logic import *
from wxmplot import PlotApp
import numpy as np
import wx.grid as gridlib


import wx

class login_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.login_title = wx.StaticText(self, -1, "LOGIN")
        self.name_prompt = wx.StaticText(self,-1,"Name:")
        self.name = wx.TextCtrl(self)
        self.pin_prompt = wx.StaticText(self, -1, "Pin Number:")
        self.pin = wx.TextCtrl(self,-1,'',style=wx.TE_PASSWORD)
        self.login = wx.Button(self, label= "log in")
        self.new = wx.Button(self, label = "Create new account")
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Arranges items vertically:

        self.sizer.Add(self.login_title, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.name_prompt, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.name,0,wx.ALL|wx.ALIGN_CENTER)
        self.sizer.Add(self.pin_prompt,0,wx.ALL|wx.ALIGN_CENTER)
        self.sizer.Add(self.pin, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.login,0,wx.ALL|wx.ALIGN_CENTER)
        self.sizer.Add(self.new,0,wx.ALL|wx.ALIGN_CENTER)
        self.SetSizer(self.sizer)

        #Event bindings for buttons

        self.new.Bind(wx.EVT_BUTTON,parent.on_createNewClick)
        self.login.Bind(wx.EVT_BUTTON, parent.on_loginClicked)

class newAccount_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.name_prompt = wx.StaticText(self, -1, "Name on Account:")
        self.name = wx.TextCtrl(self)
        self.pin_prompt = wx.StaticText(self, -1, "Pin Number:")
        self.pin = wx.TextCtrl(self, -1, '', style=wx.TE_PASSWORD)
        self.deposit_prompt = wx.StaticText(self, -1, "Initial deposit:")
        self.deposit = wx.TextCtrl(self)
        self.create = wx.Button(self, label="Create account")
        self.back = wx.Button(self, label = "Back")
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Arranges items vertically:

        self.sizer.Add(self.name_prompt, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.name, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.pin_prompt, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.pin, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.deposit_prompt, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.deposit, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.create, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.back, 0, wx.ALL | wx.ALIGN_CENTER)
        self.SetSizer(self.sizer)

        self.create.Bind(wx.EVT_BUTTON,parent.on_create_newClicked)
        self.back.Bind(wx.EVT_BUTTON, parent.on_backClicked)

class options_panel(wx.Panel):

    def __init__(self, parent, name, balance):
        wx.Panel.__init__(self, parent = parent)
        self.name = wx.StaticText(self, -1, "Hi " + name + ", Welcome back.")
        self.balance = wx.StaticText(self, -1, "Balance: £" + str(balance))
        self.withdraw = wx.Button(self, label= "Withdraw funds")
        self.deposit = wx.Button(self, label="Deposit funds")
        self.change_project = wx.Button(self, label="Change details/plot "
                                                    "projection")
        self.history = wx.Button(self, label="History")
        self.logout = wx.Button(self, label="Log out")
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Arranges items vertically:

        self.sizer.Add(self.name, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.balance, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.withdraw, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.deposit,0,wx.ALL|wx.ALIGN_CENTER)
        self.sizer.Add(self.change_project,0,wx.ALL|wx.ALIGN_CENTER)
        self.sizer.Add(self.history,0,wx.ALL|wx.ALIGN_CENTER)
        self.sizer.Add(self.logout,0,wx.ALL | wx.ALIGN_CENTER)
        self.SetSizer(self.sizer)

        self.deposit.Bind(wx.EVT_BUTTON, parent.on_depositClicked)
        self.withdraw.Bind(wx.EVT_BUTTON, parent.on_withdrawClicked)
        self.change_project.Bind(wx.EVT_BUTTON, parent.on_changeDetailsClicked)
        self.history.Bind(wx.EVT_BUTTON, parent.on_historyClicked)
        self.logout.Bind(wx.EVT_BUTTON, parent.on_logoutClicked)

class change_panel(wx.Panel):

    def __init__(self,parent, type):
        wx.Panel.__init__(self, parent = parent)
        self.balance = wx.StaticText(self, -1, "Balance: []")
        self.intro = wx.StaticText(self, -1, "Please enter " + type +
                                   " amount and press enter to confirm")
        self.amount = wx.TextCtrl(self)
        self.enter = wx.Button(self, label = "Enter")
        self.back = wx.Button(self, label="Back")
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.balance, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.intro, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.amount, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.enter, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.back, 0, wx.ALL | wx.ALIGN_CENTER)
        self.SetSizer(self.sizer)

        self.back.Bind(wx.EVT_BUTTON, parent.on_backClicked)
        self.enter.Bind(wx.EVT_BUTTON, lambda evt: parent.on_enterClicked(
            evt,type= type,amount = self.amount.GetValue()))

class details_panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.balance = wx.StaticText(self, -1, "Balance: []")
        self.intro = wx.StaticText(self, -1, "Change details & click "
                                             "plot to see a graph of "
                                             "projected earnings")
        self.interest_prompt = wx.StaticText(self, -1, "Interest (%/year):")
        self.interest = wx.TextCtrl(self)
        self.period_prompt = wx.StaticText(self, -1, "Period in months:")
        self.period = wx.TextCtrl(self)
        self.save = wx.Button(self, label="Save")
        self.plot = wx.Button(self, label="Plot")
        self.back = wx.Button(self, label = "Back")
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.balance, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.intro, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.interest_prompt, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.interest, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.period_prompt, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.period, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.save, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.plot, 0, wx.ALL | wx.ALIGN_CENTER)
        self.sizer.Add(self.back, 0, wx.ALL | wx.ALIGN_CENTER)
        self.SetSizer(self.sizer)

        self.back.Bind(wx.EVT_BUTTON, parent.on_changeBackClicked)
        self.save.Bind(wx.EVT_BUTTON, parent.on_saveClicked)
        self.plot.Bind(wx.EVT_BUTTON, parent.on_plotClicked)

class history_panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        self.back = wx.Button(self, label = "Back")

        self.back.Bind(wx.EVT_BUTTON, parent.on_changeBackClicked)

    def set_table(self,data):
        self.table = gridlib.Grid(self)
        self.table.CreateGrid(len(data),3)
        self.table.SetRowLabelSize(0)

        self.table.SetColLabelValue(0, "Balance")
        self.table.SetColLabelValue(1, "Change")
        self.table.SetColLabelValue(2, "Status")

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.back, 0, wx.ALIGN_LEFT)
        self.sizer.Add(self.table, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        for i in range (0, len(data)):
            self.table.SetCellValue(i,0,str(data[i][0]))
            self.table.SetCellValue(i,1,str(data[i][1]))
            if data[i][2] == True:
                self.table.SetCellValue(i, 2, "Successful")
            else:
                self.table.SetCellValue(i, 2, "Declined")

class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title = title, size = (400,400))
        self.login = login_panel(self)
        self.create = newAccount_panel(self)
        self.options = options_panel(self, name = "", balance = 0)
        self.dep = change_panel(self, "deposit")
        self.wit = change_panel(self, "withdrawl")
        self.details = details_panel(self)
        self.history = history_panel(self)
        self.options.Hide()
        self.create.Hide()
        self.dep.Hide()
        self.wit.Hide()
        self.details.Hide()
        self.history.Hide()
        self.statusbar = self.CreateStatusBar(1)
        self.accs = getAccounts()
        self.acc = None
        self.current_panel = self.login
        self.last_panel = None

        #Below adds panels to sizer

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.login,1,wx.EXPAND)
        self.sizer.Add(self.create, 1, wx.EXPAND)
        self.sizer.Add(self.options,1,wx.EXPAND)
        self.sizer.Add(self.dep, 1, wx.EXPAND)
        self.sizer.Add(self.wit, 1, wx.EXPAND)
        self.sizer.Add(self.details, 1, wx.EXPAND)
        self.sizer.Add(self.history, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.login.Show()
        self.Layout()

        self.statusbar.SetStatusText("test")
        self.statusbar.PushStatusText("New")
        # Code to change status text:

        self.statusbar.PushStatusText("Worked!!")

    # General functions & for changing panels

    def change_to(self, new_window):
        self.last_panel = self.current_panel
        self.current_panel.Hide()
        self.current_panel = new_window
        self.current_panel.Show()
        self.Layout()

    def on_backClicked(self,event):
        self.change_to(self.last_panel)

    # Events for login window (links to create new account & login)

    def on_createNewClick(self,event):
        self.change_to(self.create)

    def on_loginClicked(self,event):
        name = self.login.name.GetValue()
        pin = self.login.pin.GetValue()
        if canInt(pin) == False:
            self.statusbar.PushStatusText("Error: Pin can only contain "
                                          "numbers from 0-9")
        elif isName(name) == False:
            self.statusbar.PushStatusText("Error: name can only contain "
                                          "letters from a-z")
        elif isAcc(name) == False:
            self.statusbar.PushStatusText("Error: No account with name given")
        else:
            self.acc = getAcc(isAcc(name))
        if (self.acc) and self.acc.login(name = name, pin = pin) == True:
            self.options = options_panel(self, balance =
            self.acc.get_balance(), name = name)
            print (self.acc.get_history())
            self.sizer.Add(self.options, 1, wx.EXPAND)
            self.change_to(self.options)
            self.statusbar.PushStatusText("Login successful")
        else:
            self.statusbar.PushStatusText("Incorrect details")

    def on_logoutClicked(self, event):
        self.change_to(self.login)
        self.acc = None

    #Events for create new window:

    def on_create_newClicked(self,event):
        self.change_to(self.login)
        name = self.create.name.GetValue()
        pin = self.create.pin.GetValue()
        deposit = int(self.create.deposit.GetValue())

        if not isName(name):
            self.statusbar.PushStatusText("Name must contain only letters a-z.")
        elif (isAcc(name)):
            self.statusbar.PushStatusText("Account already exists!")
        elif not canInt(pin):
            self.statusbar.PushStatusText("Pin must contain only numbers 0-9")
        elif not len(pin) == 4:
            self.statusbar.PushStatusText("incorrect pin length")
        elif not canInt(deposit):
            self.statusbar.PushStatusText("deposit amount must be a number")
        else:
            self.acc = ATM(balance = deposit, name = name, pin = pin)
            newAccount(self.acc)
            self.statusbar.PushStatusText("Account creation successful")

    #Events for options window:

    def on_depositClicked(self,event):
        self.dep.balance.SetLabel("Balance: £" + str(self.acc.get_balance()))
        self.change_to(self.dep)

    def on_withdrawClicked(self,event):
        self.wit.balance.SetLabel("Balance: £" + str(self.acc.get_balance()))
        self.change_to(self.wit)

    def on_changeDetailsClicked(self,event):
        self.details.balance.SetLabel("Balance: £" + str(self.acc.get_balance()))
        self.change_to(self.details)

    def on_historyClicked(self,event):
        self.history.set_table(self.acc.get_history())
        self.change_to(self.history)
        self.Layout()

    def on_logOutClicked(self,event):
        True

    # Events for enter clicked:

    def on_enterClicked(self,event,amount, type):
        print (type)
        result = False
        if not canInt(amount):
            self.statusbar.PushStatusText(type + " amount must be a number")
        else:
            if type == "deposit":
                result = True
                self.acc.deposit(int(amount))
            else:
                result = self.acc.withdraw(int(amount))
        if not result:
            self.statusbar.PushStatusText("Insufficient funds")
        saveAcc(self.acc)
        self.statusbar.PushStatusText(type + " successful")
        print (self.acc.get_balance())
        self.options.balance.SetLabel("Balance: £" + str(self.acc.get_balance()))
        self.change_to(self.options)

    # Events for change window:

    def on_saveClicked(self,event):
        period = self.details.period.GetValue()
        interest = self.details.interest.GetValue()
        if not canInt(period) or not canInt(interest):
            self.statusbar.PushStatusText("Inputs must be a numerical only")
            return
        if int(interest)>30:
            self.statusbar.PushStatusText("More than 30% interest? Really?")
            return
        self.acc.set_period(int(period))
        self.acc.set_interest(int(interest))
        saveAcc(self.acc)
        self.statusbar.PushStatusText("Update successful")

    def on_plotClicked(self, event):
        period = self.details.period.GetValue()
        interest = self.details.interest.GetValue()
        if period == "":
            period = self.acc.get_period()
        if interest == "":
            interest = self.acc.get_interest()
        if not canInt(period) or not canInt(interest):
            self.statusbar.PushStatusText("Inputs must be a numerical only")
        if int(interest)>30:
            self.statusbar.PushStatusText("More than 30% interest? Really?")
        self.acc.set_period(int(period))
        self.acc.set_interest(int(interest))
        saveAcc(self.acc)
        data = self.acc.get_compoundData()
        self.plot_graph(data)

    def plot_graph(self,data):

        x = [i for i in range(0,len(data))]

        x_data = np.array(x)
        y_data = np.array(data)

        app = PlotApp()

        app.plot(x_data, y_data, title='Compound interest over term',
                 label='Compound interest',
                 ylabel='Funds (£)',
                 xlabel='Time (Months)')

        app.write_message('Try Help->Quick Reference')
        app.run()

    def on_changeBackClicked(self,event):
        self.change_to(self.options)

    # No events for history window

app = wx.App(False)
frame = MyFrame(None,'ATM App')
frame.Show()
app.MainLoop()