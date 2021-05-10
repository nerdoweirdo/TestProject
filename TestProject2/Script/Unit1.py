def Test1():
  TestedApps.TestedApp.Run()
  calculator = Aliases.Item.Calculator
  calculator.button2.ClickButton() #8
  calculator.button13.ClickButton() #*
  calculator.button1.ClickButton() #7
  calculator.button6.ClickButton() #5
  calculator.button14.ClickButton() #=
  result = Aliases.Item.Calculator.textBox.Text
  if (result == '600'):
    Log.Message("операция умножения двух чисел работает")
  else:
    Log.Message("операция умножения двух чисел не работает")
  Aliases.Item.Calculator.Close()
  
def Test2():
  TestedApps.TestedApp.Run()
  Aliases.Item.Calculator.button3.ClickButton() #9
  Aliases.Item.Calculator.WinFormsObject("button16").ClickButton() #%
  result = Aliases.Item.Calculator.textBox.Text
  if (result == '0,09'):
    Log.Message("взятие процента от первого числа работает")
  else:
    Log.Message("взятие процента от первого числа не работает")
  Aliases.Item.Calculator.Close()

def Test3():
  TestedApps.TestedApp.Run()
  calculator = Aliases.Item.Calculator
  calculator.button9.ClickButton() #1
  calculator.button7.ClickButton() #6
  calculator.button19.ClickButton() #sqrt
  result = calculator.textBox.Text
  if (result == '=4'):
    Log.Message("взятие кв. корня работает")
  else:
    Log.Message("взятие кв. корня не работает")
  Aliases.Item.Calculator.Close()
  

def Test4():
  TestedApps.TestedApp.Run()
  calculator = Aliases.Item.Calculator
  calculator.button2.ClickButton() #8
  calculator.button7.ClickButton() #6
  calculator.button9.ClickButton() #1
  calculator.button5.ClickButton() #4
  button = calculator.button22
  button.DblClick(62, 15) #<-(x2)
  button.DblClick(62, 15) #<-(x2)
  result = calculator.textBox.Text
  if (result == '0'):
    Log.Message("удаление элемента работает")
  else:
    Log.Message("удаление элемента не работает")
  Aliases.Item.Calculator.Close()


def Test5():
  TestedApps.TestedApp.Run()
  calculator = Aliases.Item.Calculator
  calculator.button3.ClickButton() #9
  calculator.button4.ClickButton() #+
  calculator.button9.ClickButton() #1
  calculator.button10.ClickButton() #2
  calculator.button16.ClickButton() #%
  result = calculator.textBox.Text
  if (result == '= 10,08'):
    Log.Message("операция суммы числа и процента от него работает")
  else:
    Log.Message("операция суммы числа и процента от него не работает")
  Aliases.Item.Calculator.Close()