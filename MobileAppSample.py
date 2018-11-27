from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color
#from kivy.uix.accordion import Accordion, AccordionItem
#from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from operator import itemgetter
from kivy.uix.slider import Slider

from kivy.uix.image import Image
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder
import time
from datetime import datetime,timedelta,date
 

from functools import partial,partialmethod

 

from kivy.storage.jsonstore import JsonStore


import re

import kivy
kivy.require("1.10.0")

registration = JsonStore('Registration.json')
cost = JsonStore('Specialist.json')
AdminRefer=JsonStore('Admin.json')
Order=JsonStore('AdminOrder.json')
Cash =JsonStore('Cash.json')


            



    def SpecialistWindow(self):
        global tcost
        #global getIssue
        global Mod_db
        global PDate
        global FinalDate
        global WarrnTxt
        global Name_db
        global Issue1txt
        global Model1txt
        global ListED
        global MainListED
        global SRTMainlistD
        global SRTMainlistC
        global SRTMainlistR
        global ListEDR
        global RLISTED
        global ServiceItem
        global Issue_db
        global Model_db
        global SName_db

        

        
        inLayout = GridLayout(rows=16, cols=2,height=10, size_hint=(1, 1))


        try:

                for item in registration.find(UID=userName_entered):
                    print('Issue 1 has index', item[0])             
                    
                    print('Issue1 has key  value', str(item[1]))

                    
                    Name_db = str(item[1]['Name'])                
                    print('Name_db', Name_db)

                    
            
        except IndexError as e :
                pass


        inLayout.add_widget(Label(text='[color=47ff32][b]Unique ID [/b][/color]',  markup = True,size_hint =(1,1)))        
        inLayout.add_widget(Label(text=userName_entered,size_hint =(1,1)))

        inLayout.add_widget(Label(text='[color=47ff32][b]Customer Name  [/b][/color]',  markup = True,size_hint =(1,1)))        
        inLayout.add_widget(Label(text=Name_db,size_hint =(1,1)))


        
        try:

                for item in cost.find(Service=ServiceItem):
                    print('Issue 1 has index', item[0])             
                    
                    print('Issue1 has key  value', str(item[1]))

                    
                    Mod_db = str(item[1]['Model'])                
                    

                    
            
        except IndexError as e :
                pass


        inLayout.add_widget(Label(text='[color=47ff32][b]Service[/b][/color]',  markup = True,size_hint =(1,1)))
        #SrText = TextInput(text='Mobile', multiline=False,size_hint =(1,1))
        inLayout.add_widget(Label(text=ServiceItem))

                #inLayout.add_widget(Label(text=ServiceItem))



        inLayout.add_widget(Label(text='[color=47ff32][b]Model [/b][/color]',  markup = True,size_hint =(1,1)))
        dropdown = DropDown()

        Model_list=[]
        count = 0
        Model_db =''

        for item in AdminRefer.find(ServiceName=ServiceItem):
            print('Admin has index', item[0])             
            
            print('Admin has key  value', str(item[1]))

            
            Model_db = str(item[1]['Model'])                
            print('Model_db', Model_db)       

            Model_list.append(Model_db)

            count +=1
            

        Model_set = set(Model_list)
        Model_list = list(Model_set)
        print('count',count)
        print('Model_list',Model_list)
        
        for i in range(len(Model_list)):            
            btnCust = Button(text=Model_list[i] , size_hint_y=None, height=30)
            btnCust.bind(on_release=lambda btnCust: dropdown.select(btnCust.text))
            dropdown.add_widget(btnCust)


        #mainbutton = Button(text=Model_db, size_hint=(1, 1),markup = True)
        mainbutton = Button(text='', size_hint=(1, 1),markup = True)
        inLayout.add_widget(mainbutton)
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        dropdown.bind(on_select=LoginScreen.ddSelect)
        #dropdown.bind(on_select=LoginScreen.GetUserType)

        print(' Model1txt   ',Model1txt)
        mainbutton.text=Model1txt




        
##        
        


        inLayout.add_widget(Label(text='[color=47ff32][b]Issue   [/b][/color]',  markup = True,size_hint =(1,1)))

        dropdown1 = DropDown()

        Issue_list = []
        count = 0
        Issue_db=''
        for item1 in AdminRefer.find(ServiceName=ServiceItem):
            print('Admin has index', item1[0])             
            
            print('Admin has key  value', str(item1[1]))
           
            
            Issue_db = str(item1[1]['Issue'])
            print('Issue_db', Issue_db)
            Issue_list.append(Issue_db)
            count +=1

        Issue_set = set(Issue_list)
        Issue_list = list(Issue_set)
        print('Issue_list',Issue_list)
        
        for i in range(len(Issue_list)):
            btnMod1 = Button(text=Issue_list[i] , size_hint_y=None, height=30)
            btnMod1.bind(on_release=lambda btnMod1: dropdown1.select(btnMod1.text))
            dropdown1.add_widget(btnMod1)
##        


        #mainbutton1 = Button(text=Issue_db, size_hint=(1, 1),markup = True)
        mainbutton1 = Button(text='', size_hint=(1, 1),markup = True)
        inLayout.add_widget(mainbutton1)
        mainbutton1.bind(on_release=dropdown1.open)
        dropdown1.bind(on_select=lambda instance, x: setattr(mainbutton1, 'text', x))
        dropdown1.bind(on_select=LoginScreen.dd1Select)
        print(' Issue1txt   ',Issue1txt)
        mainbutton1.text=Issue1txt

        #Select Expert
        inLayout.add_widget(Label(text='[color=47ff32][b]Select Specialist [/b][/color]',  markup = True,size_hint =(1,1)))
        Submitbutton2 = Button(text='Select Specialist', size_hint=(1, 1),markup = True)
        inLayout.add_widget(Submitbutton2)
        Submitbutton2.bind(on_press=LoginScreen.SelectExpertDetails)
        print(' SpecialistWindow SName_db ',SName_db)
        if SName_db != "" :
           Submitbutton2.text=SName_db

        
        
        

        
        



    def AdminOrderStatus(self):

        #OutLayOut = GridLayout(rows=3, cols=1,height=10, size_hint=(1, 1))

        OutLayOut = GridLayout( rows=3, cols=1,height=10, size_hint=(1, 1))

        OutLayOut.bind(minimum_height=OutLayOut.setter('height'))
        

        #inLayout2= GridLayout(rows=1, cols=13, size_hint=(.15, .15))

        inLayout2= GridLayout( cols=13, size_hint=(.15, .15))

        inLayout2.add_widget(Label(text='[color=47ff32][b]U ID [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Order \n Date[/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Customer \n Name[/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Specialist \n Name[/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Issue [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Model [/b][/color]',  markup = True,size_hint =(1,1)))        
        inLayout2.add_widget(Label(text='[color=47ff32][b]Pirority [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Payment \nRecv[/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Payment \nDone [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Delivery \nDate [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Actual \n D Date[/b][/color]',  markup = True,size_hint =(1,1)))        
        inLayout2.add_widget(Label(text='[color=47ff32][b]Warranty [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayout2.add_widget(Label(text='[color=47ff32][b]Status[/b][/color]',  markup = True,size_hint =(1,1)))

        OutLayOut.add_widget(inLayout2)

        #inLayout = GridLayout(rows=18, cols=13,height=10, size_hint=(1, 1))

        n = len(Order)
        #n=30
        entries = list(Order)

        #inLayout = GridLayout(rows=n, cols=13, height=10, size_hint=(1, 1))
        inLayout = GridLayout( cols=13, spacing=10, size_hint_y=None)

        inLayout.bind(minimum_height=inLayout.setter('height'))

        for i in range(n):

            Data =  Order.get(entries[i])
            print(Data)
            print(Data['UID'])
            

            #U1Text = TextInput(text='', multiline=False,size_hint =(.02,.1))
            U1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            U1Text.text=Data['UID']
            inLayout.add_widget(U1Text)

            #O1Text = TextInput(text='', multiline=False,size_hint =(.02,.1))
            O1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            O1Text.text=Data['OrderDate']
            inLayout.add_widget(O1Text)
            
            #C1Text = TextInput(text='', multiline=False,size_hint=(.02,.1))
            C1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            C1Text.text=Data['Customer']
            inLayout.add_widget(C1Text)
            
            
            #S1Text = TextInput(text='', multiline=False,size_hint =(.02,.1))
            S1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            S1Text.text=Data['Specailist']
            inLayout.add_widget(S1Text)     

            
            #I1Text = TextInput(text='', multiline=False,size_hint =(.02,.1))
            I1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            I1Text.text=Data['Issue']
            inLayout.add_widget(I1Text)

            #M1Text = TextInput(text='', multiline=False,size_hint =(.02,.1))
            M1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            M1Text.text=Data['Model']
            inLayout.add_widget(M1Text)
            
            #P1Text = TextInput(text='', multiline=False,size_hint=(.02,.1))
            P1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            P1Text.text=Data['Pirority']
            inLayout.add_widget(P1Text)
            
            #PR1Text = TextInput(text='', multiline=False,size_hint =(.02,.1),size=(75, 25))
            PR1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            PR1Text.text=Data['PaymentRecv']
            inLayout.add_widget(PR1Text)     

            
            
            PD1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            PD1Text.text=Data['PaymentDone']
            inLayout.add_widget(PD1Text)

            #D1Text = TextInput(text='', multiline=False,size_hint =(.02,.1),size=(75, 25))
            D1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            D1Text.text=Data['DeliveryDate']
            inLayout.add_widget(D1Text)
            
            
            AD1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            AD1Text.text=Data['ActualDDate']
            inLayout.add_widget(AD1Text)
            
            
            W1Text = Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(.02,.1))
            W1Text.text=Data['Warrenty']
            inLayout.add_widget(W1Text)     

            
            spinner = Spinner(text='Orderd',values=('Orderd', 'Provided', 'Closed', 'Cancel'),
                          size_hint=(None, None), size=(75, 25),pos_hint={'center_x': .5, 'center_y': .5})


            spinner.bind(text=LoginScreen.show_selected_value1)
            #spinner.bind(text=LoginScreen.getStatus)
            
            inLayout.add_widget(spinner)

        

        ScV = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-75))
        ScV.add_widget(inLayout)

        

        OutLayOut.add_widget(ScV)

            

        

        #BtnLayOut = GridLayout(rows=1, cols=2,height=1, size_hint=(.1,.1))
        BtnLayOut = GridLayout(rows=1, cols=2,height=1, size_hint=(.1,.1))

        Submitbutton3 = Button(text= '[color=ff3333]'+ 'Open Description' +'[/color]', markup = True, size_hint =(.1,.1),height=10 )        
        BtnLayOut.add_widget(Submitbutton3)
        Submitbutton3.bind(on_press=LoginScreen.AdminServiceDetails)

        Submitbutton4 = Button(text= '[color=ff3333]'+ 'LogOut' +'[/color]', markup = True, size_hint =(.1,.1),height=10 )        
        BtnLayOut.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=exit)

        OutLayOut.add_widget(BtnLayOut)

        



        popup = Popup(title='Order Details',size_hint=(1, 1), size=(600, 400),content=OutLayOut )
        
        popup.open()


    


    def show_selected_value1(self,text):
        global OrderStatus
        OrderStatus = text
        


    def AdminServiceDetails(self):

        OutLayOut = GridLayout(rows=4, cols=1,height=10, size_hint=(1, 1))

        inLayoutlbl = GridLayout(rows=1, cols=4,height=10, size_hint=(.1, .1))

        inLayoutlbl.add_widget(Label(text='[color=47ff32][b]Service Name [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayoutlbl.add_widget(Label(text='[color=47ff32][b]Description [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayoutlbl.add_widget(Label(text='[color=47ff32][b]Model/Code [/b][/color]',  markup = True,size_hint =(1,1)))
        inLayoutlbl.add_widget(Label(text='[color=47ff32][b]Issue [/b][/color]',  markup = True,size_hint =(1,1)))

        OutLayOut.add_widget(inLayoutlbl)
        
        inLayout = GridLayout(rows=1, cols=4,height=1, size_hint=(.1, .1))
        
        S1Text = TextInput(text='', multiline=False,size_hint =(1, 1))
        S1Text.bind(text=LoginScreen.getS)
        inLayout.add_widget(S1Text)
        
        D1Text = TextInput(text='', multiline=False,size_hint =(1, 1))
        D1Text.bind(text=LoginScreen.getD)
        inLayout.add_widget(D1Text)
        
        C1Text = TextInput(text='', multiline=False,size_hint =(1, 1))
        C1Text.bind(text=LoginScreen.getC)
        inLayout.add_widget(C1Text)     

        
        I1Text = TextInput(text='', multiline=False,size_hint =(1, 1))
        I1Text.bind(text=LoginScreen.getI)
        inLayout.add_widget(I1Text)


        OutLayOut.add_widget(inLayout)

        inLayoutlblk = GridLayout(rows=1, cols=1,height=10, size_hint=(.1, .1))

        inLayoutlblk.add_widget(Label(text='[color=47ff32][b][/b][/color]',  markup = True,size_hint =(1,1)))

        OutLayOut.add_widget(inLayoutlblk)

        LayOutbtn = GridLayout(rows=1, cols=2,height=10, size_hint=(.05, .05))

        Submitbutton4 = Button(text= '[color=ff3333]'+ 'Back' +'[/color]', markup = True, size_hint =(.1,.1),height=1 )        
        LayOutbtn.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.AdminOrderStatus)



        Submitbutton4 = Button(text= '[color=ff3333]'+ 'Save' +'[/color]', markup = True, size_hint =(.1,.1),height=1 )        
        LayOutbtn.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.AdminSave)

        OutLayOut.add_widget(LayOutbtn)   
         

        

        popup = Popup(title='Admin',size_hint=(1, 1), size=(600, 400),content=OutLayOut )
        
        popup.open()

    def getS(self,x):
        global SName
        SName = x
        print('Service Name', SName)

    def getD(self,x):
        global SDesc
        SDesc = x
        print('Desc', SDesc)

    def getC(self,x):
        global SModel
        SModel = x
        print('Model', SModel)

    def getI(self,x):
        global SIssue
        SIssue = x
        print('Issue', SIssue)



    def AdminSave(self):

        print('Data Saved stared in Admin')

        index = time.strftime("%d%m%y%H%M%S")

        AdminRefer.put(index,ServiceName = SName,Description = SDesc,Model = SModel, Issue = SIssue)

        inLayout = GridLayout(rows=2, cols=1,height=10, size_hint=(.1, .1))

        #inLayout.add_widget(Label(text='[color=47ff32][b]User Succesfully Created [/b][/color]',  markup = True,size_hint =(1,1)))

        Submitbutton4 = Button(text= '[color=47ff32]'+ 'Data Succesfully Saved' +'[/color]', markup = True, size_hint =(.1,.1) )        
        inLayout.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.AdminServiceDetails)
        popup = Popup(title='Data Saved', size_hint=(1, 1), size=(.1,.1),content=inLayout )    
        popup.open()



   


    def AdminAdd(self):
        global nMI

        nMI+=1

        LoginScreen.AdminServiceDetails(self)


    def DoSorting(self,x):

        global SortBy
        global IsCostSorted
        global IsDurSorted
        global IsRatingSorted
        global SRTMainlistD
        global SRTMainlistC
        global SRTMainlistR
        global MainListED

        SRTMainlistC.clear()
        SRTMainlistR.clear()
        SRTMainlistD.clear()
        
        SortBy = x

        if SortBy == 'Cost':

            print('sort by Cost',MainListED)
            l = len(MainListED)
            print('len',l)

            

           # print('MainListED after checkbox removed in cost' , MainListED)
            SRTMainlistC = sorted(MainListED, key=itemgetter(2))
            print('Finally Sorted SRTMainlistC ', SRTMainlistC)
            #print('Finally cost Sorted SortedMainED ', SortedMainED)
            IsCostSorted = True
            IsDurSorted = False
            IsRatingSorted = False
            
            LoginScreen.SelectExpertDetails(self)
            


        elif SortBy == 'Ratings':          

            print('sort by Rating',MainListED)
            l = len(MainListED)
            print('len',l)


            #print('MainListED after checkbox removed in Rating' , MainListED)
            SRTMainlistR = sorted(MainListED, key=itemgetter(1))
            print('Finally Sorted SRTMainlistR ', SRTMainlistR)
            #print('Finally cost Sorted SortedMainED ', SortedMainED)
            IsCostSorted = False
            IsDurSorted = False
            IsRatingSorted = True
            
            LoginScreen.SelectExpertDetails(self)
            


        elif SortBy == 'Duration':
            print('sort by Duration',MainListED)
            l = len(MainListED)
            print('len',l)
            nEel = int(l/6)
            print('nEel',nEel)



            #print('MainListED after checkbox removed in Duration' , MainListED)
            SRTMainlistD = sorted(MainListED, key=itemgetter(3) )
            print('Finally Sorted SRTMainlistD ', SRTMainlistD)
            #print('Finally Sorted SortedMainED ', SortedMainED)
            IsDurSorted = True
            IsCostSorted = False
            IsRatingSorted = False
            
            LoginScreen.SelectExpertDetails(self)
            
        

            
        

         
        
        

        
    
        
        

   
        
        
    def on_checkbox_active3(checkbox, value):
        global IsServiceAgree
        if value == False :
            IsServiceAgree = False
        elif value == True:
             IsServiceAgree = True
            
        
    def Disagree(self):

        inLayout = GridLayout(rows=2, cols=1,height=10, size_hint=(.1, .1))

        #inLayout.add_widget(Label(text='[color=47ff32][b]User Succesfully Created [/b][/color]',  markup = True,size_hint =(1,1)))

        Submitbutton4 = Button(text= '[color=47ff32]'+ 'Please tick to agree with Terms and conditions' +'[/color]', markup = True, size_hint =(.1,.1) )        
        inLayout.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.ServiceCostDetails)
        popup = Popup(title='', size_hint=(1, 1), size=(.1,.1),content=inLayout )    
        popup.open()

    def Disagree1(self):

        inLayout = GridLayout(rows=2, cols=1,height=10, size_hint=(.1, .1))

        #inLayout.add_widget(Label(text='[color=47ff32][b]User Succesfully Created [/b][/color]',  markup = True,size_hint =(1,1)))

        Submitbutton4 = Button(text= '[color=47ff32]'+ 'Please tick to agree with Terms and conditions' +'[/color]', markup = True, size_hint =(.1,.1) )        
        inLayout.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.SpecialistWindow)
        popup = Popup(title='', size_hint=(1, 1), size=(.1,.1),content=inLayout )    
        popup.open()


        
    def MessageRegistrationData(self):
        
        inLayout = GridLayout(rows=2, cols=1,height=10, size_hint=(.1, .1))

        #inLayout.add_widget(Label(text='[color=47ff32][b]User Succesfully Created [/b][/color]',  markup = True,size_hint =(1,1)))

        Submitbutton4 = Button(text= '[color=47ff32]'+ 'User Succesfully Created' +'[/color]', markup = True, size_hint =(.1,.1) )        
        inLayout.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.RegistrationWindow)
        popup = Popup(title='User Created', size_hint=(1, 1), size=(.1,.1),content=inLayout )    
        popup.open()


    def MessageData(self):
        
        inLayout = GridLayout(rows=2, cols=1,height=10, size_hint=(.1, .1))

        Submitbutton4 = Button(text= '[color=47ff32]'+ 'Ok' +'[/color]', markup = True, size_hint =(.1,.1) )        
        inLayout.add_widget(Submitbutton4)
        Submitbutton4.bind(on_press=LoginScreen.ServiceCostDetails)
        popup = Popup(title='Service', size_hint=(1, 1), size=(.1,.1),content=inLayout )    
        popup.open()
        


    def getWText(self,x):
        global WarrnTxt
        WarrnTxt = x


    def getUIDText(self,x):
        global UidTxt
        UidTxt = x

    def getSerTxt(self,x):
        global SerTxt
        SerTxt = x

    def getModTxt(self,x):
        global ModTxt
        ModTxt = x

    def getPirTxt(self,x):
        global PirTxt
        PirTxt = x
  


    def getIssTxt(self,x):
        global IssTxt
        IssTxt = x

    def getCostTxt(self,x):
        global CostTxt
        CostTxt = x
        
    def getDurText(self,x):
        global Durationn
        Durationn = x

        

    def SaveData(self):

     if IsServiceAgree == False :         
        
            LoginScreen.Disagree(self)

        else :

            index = time.strftime("%d%m%y%H%M%S")

            cost.put(index, UID=UID_db,Name=Name_db,Service=Sev_db,Model=ModTxt, Pirority=PirTxt,
                     Issue=IssTxt, Cost=CostTxt,Duration=Durationn,Warranty=WarrnTxt, Rating=rating)
        

     popup.open()  

    
    def GetCost(self,x):
        global TotalCost
        
        print(x)

        TotalCost = int(x)

        
        
        
        

        

    def GetIssue(self,x):
        global Issue
        print(x)

        Issue = x


    def GetPirority(self,p):
        global Pirority
        global FinalCost
        global IsCostPassed
        global FinalDuration
        global IsDurationPassed
        print('Pirority',p)

        Pirority = p

        entries = list(cost.find(Pirority=p))
        print('entry full list', entries)

        for x in entries:
            print(x[1])
            print('getIssue',IssueTxt)
            print('x[1]Issue',x[1]['Issue'])
            if x[1]['Issue']== IssueTxt :
                print('final cost',x[1]['Cost'])
                
                FinalCost = x[1]['Cost']
                
                IsCostPassed = True
            else :
                FinalCost=''
                IsCostPassed = False

        for y in entries:
            print(y[1])
            print('getIssue',IssueTxt)
            print('x[1]Issue',y[1]['Issue'])
            if y[1]['Issue']== IssueTxt :
                
                print('Duration' , y[1]['Duration'])
                
                FinalDuration =  y[1]['Duration'] 
                IsDurationPassed = True
            else :
                FinalDuration=''
                IsDurationPassed = False


        

        LoginScreen.SpecialistWindow(self)

                      
        
    

        
        
        
    def ErrorWindow():
            
        print('Error in Login action occured' )

        inLayout = GridLayout(rows=3, cols=1,height=10, size_hint=(1, 1))

        inLayout.add_widget(Label(text='User Name or Password is incorrect'))
        

        Submitbutton4 = Button(text= '[color=47ff32]'+ 'Login Again' +'[/color]', markup = True, size_hint =(.1,.1),height=1 )        
        inLayout.add_widget(Submitbutton4)       
        
        Submitbutton4.bind(on_press=exit)
        
        popup = Popup(title='Easy Home Error',
        content=inLayout,
        size_hint=(1, 1), size=(500, 400))        
        popup.open()    

        
    def on_text_user(instance, value):

        global userName_entered
           

        
        if value == '':
                print ('UserID empty')
        
        else: 
                
                userName_entered = value
                
                
         
    def on_text_pass(instance, valuePass):
        global IsPassWdEnter
        global passWord_entered
        if valuePass == '' :                
                IsPassWdEnter = False

        else :
              passWord_entered = valuePass              
              IsPassWdEnter = True
              

        
         
        
        
class Login:
    
    def Auth(self):

        if IsLoginPress == True :
            try:

                for item in registration.find(UID=userName_entered):
                    print('Issue 1 has index', item[0])             
                    
                    print('Issue1 has key  value', str(item[1]))

                    
                    passWord_entered_db = str(item[1]['Pass'])                
                    print('Pass', passWord_entered_db)

                    if passWord_entered_db == passWord_entered :

                        if LUserType == 'Specialist' :
                            LoginScreen.ServiceCostDetails(self)

                        

                        elif LUserType == 'Customers':

                            LoginScreen.EasyLifeWindow(self)

                        elif LUserType == 'Admin':
                            print('Admin Login')

                            LoginScreen.AdminOrderStatus(self)
                            

                        

                    else  :

                        LoginScreen.ErrorWindow()
                        
                        
            
            except IndexError as e :
                pass


            
    LoginScreen.ErrorWindow()

            

        

        elif IsLoginPress == False:            
            return None
             
             

    def bind2(self):
        
        global IsLoginPress
        if IsLoginPress == False :           
            
            IsLoginPress = True            
            submitbutton1 = Button(text='[color=ff3333] LOG-IN [/color]', size_hint=(1, 1),markup = True)       
            
            self.add_widget(submitbutton1)      
            
            
            
            submitbutton1.bind(on_press=Login.Auth)

            LogUpbutton = Button(text= '[color=47ff32]'+ 'SIGN-UP' +'[/color]', markup = True, size_hint =(1,1),height=1 )
            self.add_widget(LogUpbutton) 
            LogUpbutton.bind(on_press=LoginScreen.RegistrationWindow)
            
            
            
            
        else :

            print('in bind else IsLoginPress',IsLoginPress)
        

                
                
class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)            
             
            
            
            
                
        
                
                
    
             


class EasyLife(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    EasyLife().run()
