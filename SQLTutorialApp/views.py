from django.shortcuts import render


def homepage(request):
    return render(request, 'Homepage.html')


# Python
def py1(request):
    return render(request, 'Python\Python_BasicKnowledge.html')


def py2(request):
    return render(request, 'Python\Python_Classes.html')


def py3(request):
    return render(request, 'Python\Python_Csv&Json.html')


def py4(request):
    return render(request, 'Python\Python_File&Exception.html')


def py5(request):
    return render(request, 'Python\Python_Function.html')


def py6(request):
    return render(request, 'Python\Python_Testing_Code.html')


def py7(request):
    return render(request, 'Python\DjangoNotes.html')


# Database
def Database_connection(request):
    return render(request, 'Database\Python_Database_connection.html')


# Git
def Git(request):
    return render(request, 'Git\GIT.html')


# FFM
def layout(request):
    return render(request, "Boxme/Layout & Process.html")


def flow(request):
    return render(request, "Boxme/Fulfillment flow.html")


def rule(request):
    return render(request, "Boxme/Company Rule.html")


def standard(request):
    return render(request, "Boxme/Store Standardization.html")


def reverse_process(request):
    return render(request, "Boxme/Reverse Logistic.html")


def training(request):
    return render(request, "Boxme/Training Document.html")


def regulation(request):
    return render(request, "Boxme/Regulation.html")


def receiving(request):
    return render(request, "Boxme/Receiving Procedure.html")


def wh_controller(request):
    return render(request, "Boxme/WH Controller Procedure.html")


def picking(request):
    return render(request, "Boxme/Picking Procedure.html")


def checker(request):
    return render(request, "Boxme/Checker Procedure.html")


def packing(request):
    return render(request, "Boxme/Packing Procedure.html")


def handover(request):
    return render(request, "Boxme/Handover Procedure.html")


def returning(request):
    return render(request, "Boxme/Return Procedure.html")


def pda(request):
    return render(request, "Boxme/PDA.html")


# LX
def flow_procedure(request):
    return render(request, "Lixi/Flow & Procedures.html")


def Input_Regulation(request):
    return render(request, "Lixi/Input Regulation.html")


def Lx_Receiving(request):
    return render(request, "Lixi/Receiving.html")


def Lx_Checking(request):
    return render(request, "Lixi/QC.html")


def Lx_store(request):
    return render(request, "Lixi/Put Away.html")


def Lx_Picking(request):
    return render(request, "Lixi/Picking.html")


def Lx_Packaging(request):
    return render(request, "Lixi/Packing.html")


def Lx_Handover(request):
    return render(request, "Lixi/Handover.html")


def Lx_Return(request):
    return render(request, "Lixi/Return.html")


def allocation(request):
    return render(request, "Lixi/allocation.html")


def wms(request):
    return render(request, "Lixi/wms.html")


def vendors(request):
    return render(request, "Lixi/vendors.html")


def location(request):
    return render(request, "Lixi/Location.html")


def priority(request):
    return render(request, "Lixi/Priority.html")


def jd(request):
    return render(request, "Lixi/JD.html")


def kpi(request):
    return render(request, "Lixi/KPIs.html")


def planning(request):
    return render(request, "Lixi/Planning.html")


# Freelance
def transferimg(request):
    return render(request, "Freelance/We_transfer.html")


# Machine Learning
def Numpy(request):
    return render(request, "Machine_Learning/Numpy.html")


def Pandas(request):
    return render(request, 'Machine_Learning\Pandas.html')


def Pandas_plus_1(request):
    return render(request, 'Machine_Learning\Pandas_Adventure.html')


def Pandas_plus_2(request):
    return render(request, 'Machine_Learning\Pandas_Adventure1.html')


def Pandas_plus_3(request):
    return render(request, 'Machine_Learning\Pandas_Adventure2.html')


def Pandas_plus_4(request):
    return render(request, 'Machine_Learning\Pandas_Adventure3.html')


def Pandas_cookbook(request):
    return render(request, 'Machine_Learning\Pandas_cookbook.html')


def descriptive(request):
    return render(request, 'Machine_Learning\Descriptive_statistics.html')


# Visualization
def Plotly(request):
    return render(request, 'Data_Visualization\Plotly\Plotly.html')


def scatter(request):
    return render(request, 'Data_Visualization\Plotly\ScatterPlot.html')


def bar(request):
    return render(request, 'Data_Visualization\Plotly\Bar.html')


def line(request):
    return render(request, 'Data_Visualization\Plotly\Line.html')


def pie(request):
    return render(request, 'Data_Visualization\Plotly\Pie.html')


def bubble(request):
    return render(request, 'Data_Visualization\Plotly\Bubble.html')


def dot(request):
    return render(request, 'Data_Visualization\Plotly\Dot.html')


def fill_area(request):
    return render(request, 'Data_Visualization\Plotly\Fill Area.html')


def horizontal_bar(request):
    return render(request, 'Data_Visualization\Plotly\Horizontal_Bar.html')


def gantt(request):
    return render(request, 'Data_Visualization\Plotly\Gantt.html')


def dash(request):
    return render(request, 'Data_Visualization\Plotly\Dash.html')


# SQL_Server
def part1(request):
    return render(request, 'Database\SQL_Server\Part1.html')


def part2(request):
    return render(request, 'Database\SQL_Server\Part2.html')


def part3(request):
    return render(request, 'Database\SQL_Server\Part3.html')


def part4(request):
    return render(request, 'Database\SQL_Server\Part4.html')


def part5(request):
    return render(request, 'Database\SQL_Server\Part5.html')


def part6(request):
    return render(request, 'Database\SQL_Server\Part6.html')


def part7(request):
    return render(request, 'Database\SQL_Server\Part7.html')


def part8(request):
    return render(request, 'Database\SQL_Server\Part8.html')


def part9(request):
    return render(request, 'Database\SQL_Server\Part9.html')


def part10(request):
    return render(request, 'Database\SQL_Server\Part10.html')


def part11(request):
    return render(request, 'Database\SQL_Server\Part11.html')


def part12(request):
    return render(request, 'Database\SQL_Server\Part12.html')


# IELS
def unit1(request):
    return render(request, 'IELS/Unit1.html')


def unit2(request):
    return render(request, 'IELS/Unit2.html')


def unit3(request):
    return render(request, 'IELS/Unit3.html')


def unit4(request):
    return render(request, 'IELS/Unit4.html')


def unit5(request):
    return render(request, 'IELS/Unit5.html')


def unit6(request):
    return render(request, 'IELS/Unit6.html')


def unit7(request):
    return render(request, 'IELS/Unit7.html')


def unit8(request):
    return render(request, 'IELS/Unit8.html')


def unit9(request):
    return render(request, 'IELS/Unit9.html')


def unit10(request):
    return render(request, 'IELS/Unit10.html')


def unit11(request):
    return render(request, 'IELS/Unit11.html')


def unit12(request):
    return render(request, 'IELS/Unit12.html')


def unit13(request):
    return render(request, 'IELS/Unit13.html')


def unit14(request):
    return render(request, 'IELS/Unit14.html')


def unit15(request):
    return render(request, 'IELS/Unit15.html')


def unit16(request):
    return render(request, 'IELS/Unit16.html')


def unit17(request):
    return render(request, 'IELS/Unit17.html')


def unit18(request):
    return render(request, 'IELS/Unit18.html')


def unit19(request):
    return render(request, 'IELS/Unit19.html')


def unit20(request):
    return render(request, 'IELS/Unit20.html')


def unit21(request):
    return render(request, 'IELS/Unit21.html')


def unit22(request):
    return render(request, 'IELS/Unit22.html')


def unit23(request):
    return render(request, 'IELS/Unit23.html')


def unit24(request):
    return render(request, 'IELS/Unit24.html')


def unit25(request):
    return render(request, 'IELS/Unit25.html')


def unit26(request):
    return render(request, 'IELS/Unit26.html')


def unit27(request):
    return render(request, 'IELS/Unit27.html')


def unit28(request):
    return render(request, 'IELS/Unit28.html')


def unit29(request):
    return render(request, 'IELS/Unit29.html')


def unit30(request):
    return render(request, 'IELS/Unit30.html')


def voca1(request):
    return render(request, 'IELS/Voca1.html')


def voca2(request):
    return render(request, 'IELS/Voca2.html')


#Resume
def resume(request):
    return render(request, 'CVdesign.html')