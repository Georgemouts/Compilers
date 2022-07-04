# Giorgos Moutsopoulos Am: 4115
import sys
import os
import string

pointer = 1  # thesi deikti mes sto arxeio
global Scopeflag
Scopeflag = 0 #0 if is in programm , 1 if is in function

# ------ LEKTIKOS ANALYTIS ------
array_enomeni = []
demseymenes_lekseis = ["program", "declare", "if", "else", "while", "switchcase", "forcase", "incase", "case",
                       "defaut", "not", "and", "or", "function", "procedure", "call", "return", "in", "inout", "input",
                       "print"]
synartiseis = []


def LEX():
    array = []

    prgmend = "."  # teleiose to programma
    sep = "\n"
    inc = " "
    try:  # anoigo to programma .ci

        fileinput = open(sys.argv[1], 'r')
        print("pire to arxeio")
    except IndexError:
        print("Den diabase to arxeio")

    # Katastaseis poy mporei na synantisei kathe fora
    kat0 = 0  # gia grammata a-z, A-Z
    kat1 = 1  # gia arithmous 0-9
    kat2 = 2  # gia prakseis + , - ,*,/
    kat3 = 3  # gia telestes sysxetisis <, > ,=>,=<,<>
    kat4 = 4  # symbolo anathesis :=
    kat5 = 5  # diaxoristes ";",",";":"
    kat6 = 6  # sybmola omadopoihshs "[","]","(",")","{","}"
    kat7 = 7  # termatismos programmatos me " . "
    kat8 = 8  # diaxorismo sxoliwn me "#"
    kat10 = 10  # leykos xaraktiras
    katlath = -1  # kataskasi lathous
    eof = -2  # telos arxeiou

    state = 0

    inc = fileinput.read(1)
    while (inc != prgmend):

        # inc = fileinput.read(-1)
        # inc = fileinput.read(1)
        # print(inc)
        # print("eksoteriki while")
        # array.append(inc)
        # print(inc)
        if (inc == '\t' or inc == ' ' or inc == '\n'):
            inc = fileinput.read(1)
            continue
        if inc == ".":
            print("telos programmatos")
            break


        elif inc == " ":
            inc = fileinput.read(1)
        # print("keno")
        # continue
        # state =kat10

        elif inc.isalpha():

            state = kat0

        elif inc.isnumeric():

            state = kat1
        # print("brika arithmo")

        elif inc == "+" or inc == "-" or inc == "*" or inc == "/":
            # print("kat2")
            state = kat2

        elif inc == '<' or inc == '>' or inc == '<=' or inc == '>=' or inc == '<>' or inc == '=':
            # print("kat3")
            state = kat3

        elif inc == ':=':
            state = kat4  # mporei na einia kai katatasi 5


        elif inc == ":" or inc == ";" or inc == ",":
            state = kat5

        elif inc == '[' or inc == ']' or inc == '(' or inc == ')' or inc == '{' or inc == '}':
            state = kat6
            # print("kat6")

        elif inc == "#":
            state = kat7

        elif inc == ".":  # den tha bei pote giati ama brei "." stamataei i while
            print("BRIKA . ")
            state = kat8

        if (state == kat0 or state == kat1):  # OSO BLEPEI ALFARITHMITIKO
            # print("irthe")

            while (inc.isalpha() == True or inc.isnumeric() == True):

                if (inc == " " or inc == "."):
                    break
                array.append(inc)  # FORTONO KATHE GRAMMA SE LISTA FTIAXNO TI LEKSI         ARRAY=LEKSI
                inc = fileinput.read(1)
                # print(inc)
                # print("while tou string ")

            x = "".join(array)
            array_enomeni.append(
                x)  # FORTONO TIN LEKSI KATHE FORA STI LISTA             ARRAY_ENOMENI = LISTA APO OLES TIS LEKSEIS KAI SYMBOLA
            x = []
            array = []

        if (state == kat2):
            array_enomeni.append(inc)
            inc = fileinput.read(1)

        if (
                state == kat3):  # PROSTHETO ME TO XERI TO DEYTERO SYMBOLO AN TO DO KAI TO KATANALOSO KAI GYRNAO MIA THESI PRIN
            # print("brike SXESI")
            if (inc == "<"):
                inc = fileinput.read(1)  # perno oles tis periptoseis poy mporoyn na exoun 2 symbola
                # eksoteriki(inc,fileinput)     #KALO EKSOTERIKI SYNARTISI                       !!!!PROSORINA EKTOS !!!!

                if (inc == "="):
                    array_enomeni.append("<=")

                elif (inc == ">"):

                    array_enomeni.append("<>")
                else:
                    # inc=fileinput.seek(fileinput.tell()-1,0) #GYRNAO STO PROIGOUMENO PSIFIO
                    array_enomeni.append("<")

            elif (inc == ">"):
                inc = fileinput.read(1)
                # eksoteriki(inc, fileinput)
                if (inc == "="):
                    array_enomeni.append(">=")
                else:
                    array_enomeni.append(">")
                    inc = fileinput.seek(fileinput.tell() - 1, 0)  # GYRNAO STO PROIGOUMENO
            elif (inc == "="):
                array_enomeni.append("=")
                # inc = fileinput.seek(fileinput.tell() - 1, 0)  # GYRNAO STO PROIGOUMENO
            # print ("brika =")
            inc = fileinput.read(1)

        if (state == kat4):  # DEN THA BEI POTE GIATI AMA DEI : THA BEI STHN KAT5

            print("BRIKA:=")

        if (state == kat5 or state == kat6 or state == kat7):
            # print("brika symbolo")
            array_enomeni.append(inc)
            inc = fileinput.read(1)

    array_enomeni.append(".")  # MOLIS BGAINO AP TI WHILE PROSTHETO TIN TELEIA

    print("|--- APOTELESMA LEKTIKOU ---|")
    print(*array_enomeni, sep)


# def eksoteriki(inc,fileinput): # DEN KSERO GIATI LEITOURGEI
# print("MPIKE")
# inc=fileinput.read(1)
# print(inc)

LEX()

# --------------------------------------------------------------------------------


# ------ SYNTAKTIKOS ANALYTIS ------

currchar = 0
global Level
Level = 0
global program_name


argflag=0



global txtFile
def YACC():

    if os.path.exists("Symbol_Array.txt"):
        os.remove("Symbol_Array.txt")

    global program_name
    position = 0
    print("|-----SYNTAKTIKOS ANALYTIS------|")
    print(array_enomeni)
    print("\n")
    currchar = 0  # H THESI POY EIMAI STI LISTA ARRAY_ENOMENI

    if array_enomeni[0] == 'program':
        # CFILE()
        # INTFILE()
        if array_enomeni[1].isalpha:  # ID
            currchar = currchar + 1
            program_name = array_enomeni[currchar]
            genquad("begin_program", program_name, "_", "_")
            # print("sosti proti grammi")

            scope1=Scope(Level,8)
            scopes.append(scope1)



            print("onoma", program_name)
            currchar = 2
            if (array_enomeni[currchar] == "#"):
                currchar = comments(currchar)
                block(currchar)

            else:
                block(currchar)

        else:
            print('error: Program\'s name was expected, instead of "%s" ' % (array_enomeni[1]))
            exit(-1)
    else:
        print('error:Expexting the word "program" but couldnt found it ')
        exit(-1)


def block(currchar):  # EINAI APO TA DECLARATIONS MEXRI KAI TA PROCEDURE, FUNCTIONS
    if (array_enomeni[currchar] == "declare"):
        # print("mpaino declarations")
        currchar = declarations(currchar)

        #print("BGIKA APO DECLARATIONS TOU KENTRIKOU PROGRAMMATOS  TO EPOMENO ITEM EINAI " + array_enomeni[currchar])

        while (array_enomeni[currchar] == "function" or array_enomeni[
            currchar] == "procedure"):  # OSO BLEPEI PROCEDURE DECLARE THA TIS DIABAZEI

            if (array_enomeni[currchar] == "function"):
                currchar = function(currchar)
                currchar = currchar + 1
                #print("BGAINO APO FUNCTION ME ITEM: " + array_enomeni[currchar])

            if (array_enomeni[currchar] == "procedure"):
                currchar = procedure(currchar)

                currchar = currchar + 1

               #print("BGAINO APO PROCEDURE ME ITEM: " + array_enomeni[currchar - 1])

            if (array_enomeni[currchar] == "#"):
                currchar = comments(currchar)
                #print("BGAINO APO COMMENTS ME: " + array_enomeni[currchar])
            if (array_enomeni[currchar] == "{"):
                currchar = main(currchar)
                #print("BGAINO APO MAIN ME   " + array_enomeni[currchar])

        if (array_enomeni[currchar] == "{"):  # OTAN STAMATISOYN TA PROCEDURE KAI DECLARE MPAINEI MAIN
            print("mpaino sti main")
            currchar = main(currchar)
            main(currchar)


    else:
        print("den brike declare")
        exit(-1)


global declvars
declvars = []


def declarations(currchar):  # KANEI ELEGXO GIA KOMMATA KAI DESMEYMENES SE KATHE GRAMMI EPISTREFEI THESI TIS LISTAS OTAN TELEIONEI TO DECLARATIONS
    global declvars
    # print("mpaino declare me " + array_enomeni[currchar+1])
    while (array_enomeni[currchar] == "declare"):  # OSO BLEPO DECLARE
        while (array_enomeni[currchar] != ";"):  # KANO ELEGXO SE KATHE SEIRA MEXRI NA BRO EROTIMATIKO

            if (array_enomeni[currchar].isalnum() and array_enomeni[
                currchar] != "declare" and array_enomeni[currchar] !="="):  # PENRAO TIS METABLITES STH GLOBALVAR LISTA


                declvars.append(array_enomeni[currchar])
                #print("DECLARATIONS ", array_enomeni[currchar])
                if(Scopeflag == 0 ):
                    entity1 = Entity()
                    fentity = entity1.Variable(array_enomeni[currchar])
                    scopes[0].add_Entity(fentity)
                elif(Scopeflag == 1 ):
                    entity1 = Entity()
                    fentity = entity1.Variable(array_enomeni[currchar])
                    scopes[len(scopes)-1].add_Entity(fentity)

                # print(declvars)
            if (array_enomeni[currchar] == ","):
                # print ("brika komma")

                if (array_enomeni[currchar - 1].isalnum() != True or array_enomeni[
                    currchar + 1].isalnum() != True):  # ELEGXO GIA KOMMATA
                    print("Error in declarations check your variables.")
                    exit(-1)

                if (array_enomeni[currchar - 1] in demseymenes_lekseis):  # KANO ELEGXO GIA  DESMEYMENES LEKSEIS
                    i = 0
                    while i < 100:
                        if (array_enomeni[currchar - 1] == demseymenes_lekseis[i] or array_enomeni[currchar + 1] ==
                                demseymenes_lekseis[i]):
                            print("Error you used the forbidden word in declarations:   " + demseymenes_lekseis[i])
                            exit(-1)
                        i = i + 1

            # print (array_enomeni[currchar])
            currchar = currchar + 1
        currchar = currchar + 1

        if (array_enomeni[currchar] == "#"):
            currchar = comments(currchar)
            if (array_enomeni[currchar] == "declare"):
                print(
                    "Please use comments before or after declarations and in one sentence, NOT an ERROR but I cannot handle it")
                # exit(-1)

    return currchar


def func_proce_declarations(currchar,
                            funcname):  # H DIAFORA EINAI OTI EDO EINAI TOPIKES METABLITES KAI PREPEI NA KRATAO KAI TO ONOMA THS SYNARTHSHS
    # print("mpaino declare_func_proceS me " + array_enomeni[currchar + 1])
    while (array_enomeni[currchar] == "declare"):  # OSO BLEPO DECLARE
        while (array_enomeni[currchar] != ";"):  # KANO ELEGXO SE KATHE SEIRA MEXRI NA BRO EROTIMATIKO

            if (array_enomeni[currchar].isalnum() and array_enomeni[
                currchar] != "declare"):  # PENRAO TIS METABLITES STH GLOBALVAR LISTA
                # print("PRIN MPEI STO RECORD", array_enomeni[currchar])
                if (Scopeflag == 0):
                    entity1 = Entity()
                    fentity = entity1.Variable(array_enomeni[currchar])
                    scopes[len(scopes) - 2].add_Entity(fentity)
                elif (Scopeflag == 1):
                    entity1 = Entity()
                    fentity = entity1.Variable(array_enomeni[currchar])
                    scopes[len(scopes) - 1].add_Entity(fentity)
                declvars.append(array_enomeni[currchar])
                # Record_Entity(funcname, " ", " ", "", array_enomeni[currchar], " ") PROSOXI  PINAKAS SYMBOLWWWN

            if (array_enomeni[currchar] == ","):
                # print ("brika komma")

                if (array_enomeni[currchar - 1].isalnum() != True or array_enomeni[
                    currchar + 1].isalnum() != True):  # ELEGXO GIA KOMMATA
                    print("Error in declarations check your variables.")
                    exit(-1)

                if (array_enomeni[currchar - 1] in demseymenes_lekseis):  # KANO ELEGXO GIA  DESMEYMENES LEKSEIS
                    i = 0
                    while i < 100:
                        if (array_enomeni[currchar - 1] == demseymenes_lekseis[i] or array_enomeni[currchar + 1] ==
                                demseymenes_lekseis[i]):
                            print("Error you used the forbidden word in declarations:   " + demseymenes_lekseis[i])
                            exit(-1)
                        i = i + 1

            # print (array_enomeni[currchar])
            currchar = currchar + 1
        currchar = currchar + 1

        if (array_enomeni[currchar] == "#"):
            currchar = comments(currchar)
            if (array_enomeni[currchar] == "declare"):
                print(
                    "Please use comments before or after declarations and in one sentence, NOT an ERROR but I cannot handle it")
                # exit(-1)

    return currchar


def procedure(currchar):
    global argflag
    global txtFile
    global offset
    global Level
    global Scopeflag
    tmp = 0
    Scopeflag = 1
    #print("mpika procedure " + array_enomeni[currchar + 1])
    funcname = array_enomeni[currchar + 1]
    genquad("begin_procedure", funcname, "_", "_")

    Scopeflag = 1

    #print("Onoma Scope", scopes)
    #WriteSymbol_Table(funcname, 0)

    synartiseis.append(funcname)
    formalparlist = []
    # print("MPIKA STI FUNCTION ME ITEM   " + array_enomeni[currchar])
    if (array_enomeni[currchar + 1].isalnum() != True):
        print("Error missing name of a procedure")
        exit(-1)
    if (array_enomeni[currchar + 2] != "("):  # KANO ELEGXO GIA (
        print("Error:  missing '(' from your function's: --" + array_enomeni[currchar + 1] + "-- initialization")
        exit(-1)
    currchar = currchar + 2
    if (array_enomeni[currchar] == "("):  # KANO ELEGXO GIA )
        symbolcheck(currchar)

        currchar = currchar + 1
        Level = Level + 1
        scope1 = Scope(Level, 8)
        entity1 = Entity()

        tmp = offset
        fentity = entity1.SubProgram(funcname, "int", nextquad(), formalparlist, 0)
        scopes[-1].add_Entity(fentity)
        scopes.append(scope1)

        deleteOffset()


        currchar = currchar + 1
        while (array_enomeni[currchar] != ')'):  # BAZO TIS METABLITES EISODOU SE LISTA formalparlist
            formalparlist.append(array_enomeni[currchar])

            if (array_enomeni[currchar] == "in"):
                argflag = 1
                entity1 = Entity()
                fentity = entity1.Parameter(array_enomeni[currchar + 1], "in")
                scopes[len(scopes) - 1].add_Entity(fentity)
                argflag = 0
            if (array_enomeni[currchar] == "inout"):
                argflag = 1
                entity1 = Entity()
                fentity = entity1.Parameter(array_enomeni[currchar + 1], "inout")
                scopes[len(scopes) - 1].add_Entity(fentity)
                argflag = 0

            currchar = currchar + 1
        currchar = currchar + 1  # PAO MIA THESI META TA ORISMATA
        # print(array_enomeni[currchar])

        if (array_enomeni[currchar] == "{"):  # KANO ELEGXO GIA {
            print(array_enomeni[currchar])
            symbolcheck(currchar)
            currchar = currchar + 1

            #print("DECLARE MESA STO PROCEDURE:" + array_enomeni[currchar + 1])
            currchar = func_proce_declarations(currchar, funcname)
            currchar = currchar - 1

            # print("edo " + array_enomeni[currchar + 1])
            # returncheck(currchar)  # --- DEN KANO ELEGXO GIA RETURN---
            # print(array_enomeni[currchar])
            currchar = STATEMENTS(currchar)  # MPAINO SE MAIN KAI OXI STATEMENTS
            genquad("end_procedure", funcname, "_", "_")



            Scopeflag = 0

            q = 0
            for i in scopes:
                print("Scope", q, "-------")
                q = q + 1
                for j in i.entityList:
                    print(str(j.name) + "/" + str(j.offset) + "->")
            print("\n \n")
            return currchar


def function(currchar):
    global argflag
    global txtFile
    global offset
    global Level
    global Scopeflag
    tmp = 0
    Scopeflag=1
    #print("mpika function " + array_enomeni[currchar + 1])
    funcname = array_enomeni[currchar + 1]
    genquad("begin_function", funcname, "_", "_")

    #fileptr =txtFile.tell()     #PAIRNO TO TELOS TOU PROHGOUMENOU
    #print("APOTELESMA TELL", fileptr)


    #fileptr = txtFile.tell()
    #print("APOTELESMA TELL 2O SCOPE",fileptr)

    synartiseis.append(funcname)
    formalparlist = []
    # print("MPIKA STI FUNCTION ME ITEM   " + array_enomeni[currchar])
    if (array_enomeni[currchar + 2] != "("):  # KANO ELEGXO GIA (
        print("Error:  missing '(' from your function's: --" + array_enomeni[currchar + 1] + "-- initialization")
        exit(-1)
    currchar = currchar + 2
    if (array_enomeni[currchar] == "("):  # KANO ELEGXO GIA )
        symbolcheck(currchar)

        currchar = currchar + 1
        Level = Level + 1
        scope1 = Scope(Level, 8)
        entity1 = Entity()

        tmp = offset
        fentity = entity1.SubProgram(funcname, "int", nextquad(), formalparlist, 0)
        scopes[-1].add_Entity(fentity)
        scopes.append(scope1)

        deleteOffset()
        while (array_enomeni[currchar] != ')'):  # BAZO TIS METABLITES EISODOU SE LISTA formalparlist
            formalparlist.append(array_enomeni[currchar])

            if(array_enomeni[currchar]== "in" ):
                argflag =1
                entity1 = Entity()
                fentity = entity1.Parameter(array_enomeni[currchar + 1],"in")
                scopes[len(scopes) - 1].add_Entity(fentity)
                argflag=0
            if (array_enomeni[currchar] == "inout"):
                    argflag=1
                    entity1 = Entity()
                    fentity = entity1.Parameter(array_enomeni[currchar + 1],"inout")
                    scopes[len(scopes) - 1].add_Entity(fentity)
                    argflag =0

            # print("FORMAL LIST PRINT")
            #print(formalparlist)  # PAIRNO TA ORISMATA MESA STIN PARENTHESI TIS FUNC
            currchar = currchar + 1
        currchar = currchar + 1  # PAO MIA THESI META TA ORISMATA
        # print(array_enomeni[currchar])

        if (array_enomeni[currchar] == "{"):  # KANO ELEGXO GIA {
            # print(array_enomeni[currchar])
            symbolcheck(currchar)
            currchar = currchar + 1
            #print("DECLARE MESA STO FUNCTION:" + array_enomeni[currchar + 1])
            currchar = func_proce_declarations(currchar, funcname)
            currchar = currchar - 1


            returncheck(currchar)  # ---KANO ELEGXO GIA RETURN---

            currchar = STATEMENTS(currchar)



            genquad("end_function", funcname, "_", "_")

            offset = tmp +2
            Scopeflag =0

            q = 0
            for i in scopes:
                print("Scope", q, "-------")
                q = q + 1
                for j in i.entityList:
                    print(str(j.name) + "/" + str(j.offset) + "->")
            print("\n \n")

            return currchar


def main(currchar):
    # print("mpika main")
    global txtFile
    while (array_enomeni[currchar] != "."):
        if (array_enomeni[currchar] == "procedure"):
            procedure(currchar)
        if (array_enomeni[currchar] == "function"):
            function(currchar)

        if (array_enomeni[currchar] == "program" or array_enomeni[currchar] == "default" or array_enomeni[
            currchar] == "or" or array_enomeni[currchar] == "and" or array_enomeni[currchar] == "not"
                or array_enomeni[currchar] == "function" or array_enomeni[currchar] == "procedure" or array_enomeni[
                    currchar] == "in" or array_enomeni[currchar] == "inout"):
            print("Error: forbidden word : " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "if"):
            currchar = IFSTATE(currchar)
        elif (array_enomeni[currchar] == "else"):
            print("Error:You should insert if statement before else: ")
            exit(-1)
        elif (array_enomeni[currchar] == "while"):  # TO WHILE EPISTREFEI MIA THESI META TO } TOY
            #print("MPAINO STI WHILE ME : " + array_enomeni[currchar])
            currchar = WHILESTATE(currchar)
            #print("Bgaino apo while me: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "switchcase"):
            currchar = SWITCHSTATE(currchar)
        elif (array_enomeni[currchar] == "forcase"):
            currchar = FORCASESTATE(currchar)
            #print("BGAINO APO FOR ME: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "incase"):
            currchar = INCASE(currchar)
            #print("BGAINO APO INCASE ME:  " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "call"):
            currchar = CALLSTATE(currchar)
        elif (array_enomeni[currchar] == "input"):
            INPUTSTATE(currchar)
        elif (array_enomeni[currchar] == "print"):
            PRINTSTATE(currchar)
        elif (array_enomeni[currchar] == "="):
            print("Error Missing ':' before '=': " + array_enomeni[currchar - 1])
            exit(-1)
        elif (array_enomeni[currchar] == ":"):
            currchar = currchar + 1
            if (array_enomeni[currchar] == "="):
                # print("MPAINO ASSIGN")
                currchar = ASSIGNSTATE(currchar)
                # print("Bgaino apo assign me ", array_enomeni[currchar])
            else:
                print("Error : missing '=' in variable: " + array_enomeni[currchar - 2])
                exit(-1)
        currchar = currchar + 1
    # print(array_enomeni[currchar])
    genquad("end_program", program_name, "_", "_")
    print("BRIKA TELEIA TELOS PROGRAMMATOS , OLA KALA ")
    CFILE()
    INTFILE()
    Write_Symbol_Table()
    final()

    q = 0
    for i in scopes:
        print("Scope", q,"-------")
        q = q + 1
        for j in i.entityList:
            print(str(j.name) + "/" + str(j.offset) + "->")

    exit(1)
    # return currchar        #AYTO EDO EINAI TO LATHOS STO PROGRAMMA


def comments(currchar):  # DIABAZEI TA SXOLIA KAI GYRNAEI MIA THESI META TO #
    # print("brika #")
    # print(array_enomeni[currchar+1])
    currchar = currchar + 1
    while (array_enomeni[currchar] != "#"):  # OSO DEN BLEPEI # SYNEXIZEI
        currchar = currchar + 1
        if (array_enomeni[currchar] == "#"):
             #print("brika2o #")
             return currchar + 1
        elif(array_enomeni[currchar]=="{" or array_enomeni[currchar] == "."):
            print("Error : couldnt find second #")
            exit(-1)
        # currchar =currchar+1


def returncheck(currchar):  # ELEGXEI GIA RETURN MESA STI FUNCTION
    while (array_enomeni[currchar] != "}"):
        # print(array_enomeni[currchar])
        if (array_enomeni[currchar] == "return"):
            # print("brika return")
            return
        if (array_enomeni[currchar] == "procedure" or array_enomeni[currchar] == "function"):
            print("Error:Return not found in your function")
            exit(-1)
        currchar = currchar + 1
    if (array_enomeni[currchar] == "}"):
        print("Error:Return not found in your function")
        exit(-1)


def symbolcheck(currchar):  # ELEGXEI () {} [] EXEI THEMATA ME TO (()) {{}} [[]]

    if (array_enomeni[currchar] == "("):
        while (array_enomeni[currchar] != ")"):
            # print(array_enomeni[currchar])
            if (array_enomeni[currchar] == ")"):
                # print("brika deyteri )")
                return currchar
            # currchar=currchar+1
            elif (array_enomeni[currchar] == "{" or array_enomeni[currchar] == ";"):
                print("Error: couldnt find the ')' last characters were:    " + array_enomeni[currchar - 3] +
                      array_enomeni[currchar - 2] + array_enomeni[currchar - 1])
                exit(-1)
            else:
                currchar = currchar + 1
        if (array_enomeni[currchar] == ")"):
            # print("BRIKA DEYTERI")
            # print(currchar)
            return currchar

    if (array_enomeni[currchar] == "{"):
        currchar = currchar + 1
        # print(array_enomeni[currchar])
        while (array_enomeni[currchar] != "{" and array_enomeni[currchar] != "."):
            # print(array_enomeni[currchar])
            if (array_enomeni[currchar] == "}"):
                # print("brika deyteri }")
                return currchar
            currchar = currchar + 1
            if (array_enomeni[currchar] == "{" or array_enomeni[currchar] == "."):
                print("Error: couldnt find the '}' last characters were:    " + array_enomeni[currchar - 1] +
                      array_enomeni[currchar - 2] + array_enomeni[currchar - 3])
                exit(-1)


global temporary_variables

temporary_variables = 0
global false_position_list
global true_position_list


def condition(currchar):
    global false_position_list
    global true_position_list
    global temporary_variables
    # false_position
    flag = 0
    # print("MPIKA CONDITIONS" + array_enomeni[currchar])
    currchar = currchar + 1
    # print("PRIN MPO WHILE" + array_enomeni[currchar])
    start = currchar  # KRATAO TI THESI THS ARXHS TOU CONDITION
    global token
    truelist = []

    while (array_enomeni[currchar] != ")"):  # APO TON PINAKA SYMBOLON KANE TO TRUE FALSE STHN EPOMENH FASH
        if (array_enomeni[currchar] == "or"):
            boolTerm(currchar, "or")
            flag = 1

        elif (array_enomeni[currchar] == "and"):
            boolTerm(currchar, "and")
            flag = 1

        currchar = currchar + 1
    if (flag == 0):
        currchar = start  # KSANA ARXIZO APO TIN ARXI THS CONDITION AN DEN EXEI AND H OR
        while (array_enomeni[currchar] != ")"):
            #print("DEN EXEI OR H AND " + array_enomeni[currchar])
            currchar = currchar + 1
    # backPatch(truelist, nextquad() + 1)

    true_position_list = quad_list[
        len(quad_list) - 1]  # KRATAEI TH THESH TOU CONDITION STH QUADLIST AMA THELO NA TO XRISIMOPOIHSO GIA LOOPES
    #print("KRATAEI TO ", true_position_list)

    genquad("jump", "_", "_", nextquad() + 2)  # AN TO CONDITION EINAI TRUE
    genquad("jump", "_", "_", "_")  # AN TO CONDITION EINAI FALSE

    false_position_list = quad_list[
        len(quad_list) - 1]  # KRATAO TH LITA POY EINAI FALSE KAI TO PROTO STOIXEIO EINAI TO ID TOY
    #print("TYPOMA THESHS FALSE JUMP ", false_position_list)
    # print("META TO  IF" ,array_enomeni[currchar])

    return currchar


def boolTerm(currchar, andor):  # EXO BREI TO OR H TO AND
    # print("MPIKA STO BOOLTERM " + array_enomeni[currchar])
    orposition = currchar
    boolfactor1 = []  # H LISTA APO TA DEKSIA THS BOOLTERM
    boolfactor2 = []  # H LISTA APO TA ARISTERA THS BOOLTERM
    currchar = currchar + 1
    while (array_enomeni[currchar] != "and" and array_enomeni[currchar] != "or" and array_enomeni[
        currchar] != ")"):  # BAZO SE LISTA TO 2O BOOLFACTOR

        # print("eimai sto +" +array_enomeni[currchar])
        boolfactor1.append(array_enomeni[currchar])
        currchar = currchar + 1

    endposition = currchar  # EDO TELEIONEI TO 2O BOOLFACTOR TOU OR
    currchar = orposition
    currchar = currchar - 1

    while (array_enomeni[currchar] != "(" and array_enomeni[currchar] != "and" and array_enomeni[
        currchar] != "or"):  # BAZO SE LISTA TO PROTO BOOLFACTOR
        boolfactor2.append(array_enomeni[currchar])
        currchar = currchar - 1

    boolfactor2.reverse()

    # print(boolfactor1)
    # print(boolfactor2)
    boolFactor(boolfactor1)
    boolFactor(boolfactor2)
    # print("BGAINO APO BOOLTERM ME " +array_enomeni[endposition])
    returnlist = [endposition, "true"]
    return returnlist


def boolFactor(
        boolfactor):  # DHMIOURGEI TA GENQUAD GIA SYMBOLA < > <= >= <> KAI ME PAEI KAI STHN EXPRESSION GIA NA PERASO TA GENQUADS
    # print("MPIKA BOOLFACTOR " + array_enomeni[currchar])
    i = 0
    print(boolfactor)
    expression1 = []
    expression2 = []
    while (boolfactor[i] != ">" and boolfactor[i] != "<" and boolfactor != "=" and boolfactor != "<=" and boolfactor[
        i] != ">=" and boolfactor[i] != "<>" and boolfactor[i] != "="):
        expression1.append(boolfactor[i])
        i = i + 1
    symbol = boolfactor[i]
    # print(symbol)
    # print(i)
    i = i + 1
    while (i < len(boolfactor)):
        expression2.append(boolfactor[i])
        i = i + 1
    # print(expression1)
    # print (expression2)

    T1 = expression(expression1)
    T2 = expression(expression2)
    print(T1, T2)
    genquad(symbol, T1, T2, nextquad() + 1)  # BAZEI STH GENQUAD TIS SXESEIS ANAMESA STA T_I KAI STA MUL_OP

    return currchar


def expression(expressionlist):
    # print(expressionlist)
    i = 0
    k = newTemp()
    while (i < len(expressionlist)):
        if (expressionlist[i] == "+"):

            genquad("+", expressionlist[i - 1], expressionlist[i + 1], k)

        elif (expressionlist[i] == "-"):

            genquad("-", expressionlist[i - 1], expressionlist[i + 1], k)
        elif (expressionlist[i] == "*"):

            genquad("*", expressionlist[i - 1], expressionlist[i + 1], k)

        elif (expressionlist[i] == "/"):

            genquad("/", expressionlist[i - 1], expressionlist[i + 1], k)
        i = i + 1
    return k


def IFSTATE(currchar):  # PREPEI PROTA IF META ELSE ALLIOS ERROR
    global false_position_list
    currchar = currchar + 1
    # print("mpaino sto if: "+array_enomeni[currchar])
    symbolcheck(currchar)  # KANEI ELEGXO GIA PARENTHESEIS
    #print("EIMAI STO IF ME " + array_enomeni[currchar] + array_enomeni[currchar+1])

    currchar = condition(currchar)
    #print("GYRNAO APO IF ME" +array_enomeni[currchar])
    currchar = currchar + 1
    symbolcheck(currchar)  # KANEI ELEGXO GIA AGGISTRA
    currchar = STATEMENTS(currchar)
    #print("STATEMENTS STO IF" + array_enomeni[currchar])
    currchar = currchar + 1
    #print("BGAINO APO TO IF ME: " + array_enomeni[currchar])
    if (array_enomeni[currchar] == "else"):  # KANEI ELEGO GIA ELSE
        # print("BRIKA ELSE: "+array_enomeni[currchar])
        backPatch(false_position_list, nextquad())
        currchar = currchar + 1
        symbolcheck(currchar)  # KANEI ELEGXO GIA AGGISTRA
        currchar = STATEMENTS(currchar)
        # print("BGAINO APO TO ELSE ME: " + array_enomeni[currchar])
        # currchar = currchar +1
        return currchar
    else:
        print("Error couldnt find else in if statement: ")
        exit(-1)


def WHILESTATE(currchar):  # ELEGXO PARENTHESEIS AGKISTRA KAI GYRNAO MIA THESI META TO TELEYTAIO
    currchar = currchar + 1
    # print("prin bo" +array_enomeni[currchar])
    symbolcheck(currchar)  # KANEI ELEGXO GIA PARENTHESEIS
    currchar = condition(currchar)
    # print("meta to symbolcheck " + array_enomeni[currchar])
    currchar = currchar + 1  # GYRIZEI MIA THESI META  TIN PARENTHESI
    # print("prin bei " + array_enomeni[currchar])
    # STATEMENTS(currchar)
    symbolcheck(currchar)  # ELEGXO AGGISTRA
    currchar = STATEMENTS(currchar)
    backPatch(false_position_list, nextquad())
    genquad("jump", "_", "_", true_position_list[0])
    # print("bgaino apo statements tou while me : " +array_enomeni[currchar])

    return currchar


def SWITCHSTATE(currchar):
    # print ("Mpaino Switchcase me " +array_enomeni[currchar])
    currchar = currchar + 1
    symbolcheck(currchar)
    print("PRIN MPO STO CASE ", array_enomeni[currchar])
    if (array_enomeni[currchar] == "case"):  # KANO ELEGXO GIA CASE
        currchar = currchar + 1
        symbolcheck(currchar)  # KANEI ELEGXO GIA PARENTHESEIS

        currchar = condition(currchar)
        currchar = currchar + 1
        #print("BGAINO APO CASE:", array_enomeni[currchar])
        currchar = STATEMENTS(currchar)  # BGAINO APO TO CASE
        currchar = currchar + 1
        backPatch(false_position_list, nextquad())

        if (array_enomeni[currchar] == "case"):  # KANO ELEGXO GIA CASE
            currchar = currchar + 1
            symbolcheck(currchar)  # KANEI ELEGXO GIA PARENTHESEIS

            currchar = condition(currchar)
            currchar = currchar + 1
            #print("BGAINO APO CASE:", array_enomeni[currchar])
            currchar = STATEMENTS(currchar)  # BGAINO APO TO CASE
            currchar = currchar + 1
            backPatch(false_position_list, nextquad())

            if (array_enomeni[currchar] == "case"):  # KANO ELEGXO GIA CASE
                currchar = currchar + 1
                symbolcheck(currchar)  # KANEI ELEGXO GIA PARENTHESEIS

                currchar = condition(currchar)
                currchar = currchar + 1
                print("BGAINO APO CASE:", array_enomeni[currchar])
                currchar = STATEMENTS(currchar)  # BGAINO APO TO CASE
                currchar = currchar + 1
                backPatch(false_position_list, nextquad())

        if (array_enomeni[currchar] == "default"):
            currchar = currchar + 1
            # print(array_enomeni[currchar])
            currchar = DEFAULTSTATEMENTS(currchar)

            return currchar
        else:
            print("Error: Couldnt find the default in switchcase ")
    else:
        print("Error:Couldnt find case in switchcase")
        exit(-1)


def FORCASESTATE(currchar):
    print("MPAINO STO FORCASE ME : " + array_enomeni[currchar])
    currchar = currchar + 1

    symbolcheck(currchar)
    # currchar = currchar + 1
    if (array_enomeni[currchar] == "case"):  # KANO ELEGXO GIA  CASE
        currchar = currchar + 1
        #print("EIMAI STO CASE " + array_enomeni[currchar])

        currchar = condition(currchar)
        currchar = currchar + 1
        #print("BGAINO APO CASE:" + array_enomeni[currchar])
        currchar = CASESTATEMENTS(currchar)  # BGAINO APO TO CASE
        backPatch(false_position_list, nextquad())
        genquad("jump", "_", "_", true_position_list[0])
        #print("Bgaino apo statements me:  " + array_enomeni[currchar])

        #print("PRIN TO DEFAULT BLEPO " + array_enomeni[currchar])
        if (array_enomeni[currchar] == "default"):
            currchar = currchar + 1
            currchar = DEFAULTSTATEMENTS(
                currchar)  # TA STATEMENTS TELEIONOUN MEXRI TO EROTHMATIKO KAI OXI MEXRI TIN PARENTHESI
            # print(array_enomeni[currchar])
            return currchar
        else:
            print("Error: Couldnt find the default in forcase ")
            exit(-1)
    else:
        print("Error:Couldnt find case in forcase")
        exit(-1)


def INCASE(currchar):
    # print("Mpaino INCASE ME : " + array_enomeni[currchar])
    currchar = currchar + 1
    symbolcheck(currchar)

    if (array_enomeni[currchar] == "case"):
        print(array_enomeni[currchar])
        currchar = currchar + 1
        currchar = condition(currchar)
        # print("META TO CASE: " + array_enomeni[currchar])
        currchar = currchar + 1
        currchar = STATEMENTS(currchar)
        currchar = currchar + 1
        backPatch(false_position_list, nextquad())
        if (array_enomeni[currchar] == "case"):
            currchar = currchar + 1
            currchar = condition(currchar)
            # print("META TO CASE: " + array_enomeni[currchar])
            currchar = currchar + 1
            currchar = STATEMENTS(currchar)
            currchar = currchar + 1
            backPatch(false_position_list, nextquad())
            if (array_enomeni[currchar] == "case"):
                currchar = currchar + 1
                currchar = condition(currchar)
                # print("META TO CASE: " + array_enomeni[currchar])
                currchar = currchar + 1
                currchar = STATEMENTS(currchar)
                currchar = currchar + 1
                backPatch(false_position_list, nextquad())
                if (array_enomeni[currchar] == "case"):
                    currchar = currchar + 1
                    currchar = condition(currchar)
                    # print("META TO CASE: " + array_enomeni[currchar])
                    currchar = currchar + 1
                    currchar = STATEMENTS(currchar)
                    currchar = currchar + 1
                    backPatch(false_position_list, nextquad())
    if (array_enomeni[currchar] == "default"):
        # print("EIMAI STO DEFAULT")
        # backPatch(false_position_list,nextquad())

        currchar = currchar + 1
        currchar = DEFAULTSTATEMENTS(currchar)
        # print("META  APO CASE STATEMENTS" +array_enomeni[currchar])
        return currchar


    else:
        print("Error:Missing case from incase")
        exit(-1)
    return


def assigncall(currchar):  # KALESMA SYNARTHSHS ME ISOTHTA
    #print("EIMAI STO " + array_enomeni[currchar])
    # print("MPIKA ASSIGNCALL " + array_enomeni[currchar])

    funcname = array_enomeni[currchar]  # PAIRNO TO ONOMA THS SYNARTHSHS
    currchar = currchar + 2

    while (array_enomeni[currchar] != ";"):
        if (array_enomeni[currchar] == "in"):
            # print("EIMAI STO " + array_enomeni[currchar])
            genquad("par", array_enomeni[currchar + 1], "cv", "_")  # IN = CV
            currchar = currchar + 1

        if (array_enomeni[currchar] == "inout"):
            # print("Eimai sto " +array_enomeni[currchar])
            genquad("par", array_enomeni[currchar + 1], "ref", "_")  # INOUT = PAR
            currchar = currchar + 1

        currchar = currchar + 1
    genquad("call", funcname, "_", "_")
    return currchar


def operations(currchar):  # DEN DOULEYEI H PROTERAIOTHTA !!!!
    global temporary_variables
    # print("BRIKA OP " +array_enomeni[currchar+1] , array_enomeni[currchar])
    begin = currchar - 3

    # print("MPAINO WHILE ME "+array_enomeni[currchar])

    if (array_enomeni[currchar] == "(" or array_enomeni[currchar] == ")"):  # AN BREI PARENTHESI NA SYNEXEISEI

        symbolcheck(currchar)
        currchar = currchar + 1
        # print("BRHKA PARENTHESI     " + array_enomeni[currchar])

    if (array_enomeni[currchar + 1] == "+"):
        # print("EIMAI STO SYN ME " + array_enomeni[currchar])
        if (array_enomeni[currchar + 2] == "(" or array_enomeni[currchar + 2] == ")"):
            currchar = currchar + 1

        k = newTemp()
        genquad("+", array_enomeni[currchar - 1], array_enomeni[currchar + 2], k)
        currchar = currchar + 2
        temporary_variables = temporary_variables + 1



    elif (array_enomeni[currchar + 1] == "-"):
        if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
            currchar = currchar + 1
        k = newTemp()
        genquad("-", array_enomeni[currchar], array_enomeni[currchar + 2], k)
        currchar = currchar + 2
        temporary_variables = temporary_variables + 1

    elif (array_enomeni[currchar + 1] == "*"):
        if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
            currchar = currchar + 1
        k = newTemp()
        genquad("*", array_enomeni[currchar], array_enomeni[currchar + 2], k)
        currchar = currchar + 2
        temporary_variables = temporary_variables + 1

    elif (array_enomeni[currchar + 1] == "/"):
        if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
            currchar = currchar + 1
        k = newTemp()
        genquad("/", array_enomeni[currchar], array_enomeni[currchar + 2], k)
        currchar = currchar + 2
        temporary_variables = temporary_variables + 1

    elif (array_enomeni[currchar] == ";"):
        print("BGAINO APO TH WHILE THS OPERATIONS " + array_enomeni[currchar])

    currchar = currchar + 1

    while (array_enomeni[currchar] != ";"):

        if (array_enomeni[currchar] == "(" or array_enomeni[currchar] == ")"):  # AN BREI PARENTHESI NA SYNEXEISEI
            symbolcheck(currchar)
            #print("BRHKA PARENTHESI     " + array_enomeni[currchar])
            currchar = currchar + 1

        if (array_enomeni[currchar] == "+"):
            if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
                currchar = currchar + 1
            if (array_enomeni[currchar + 1] in synartiseis):  # AMA BRO SYNARTHSH POU YPARXEI  STH LYSTA
                #print("BRHKA SYNARTHSH")
                k = newTemp()
                currchar = currchar + 1
                funcname = array_enomeni[currchar]
                genquad("+", T_variables[temporary_variables - 1], funcname, k)
                currchar = currchar + 1  # anoigma parenthesis]
                temporary_variables = temporary_variables + 1

                while (array_enomeni[currchar] != ")"):
                    if (array_enomeni[currchar] == "in"):
                        # print("EIMAI STO " + array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "cv", "_")  # IN = CV
                        currchar = currchar + 1
                    if (array_enomeni[currchar] == "inout"):
                        # print("Eimai sto " +array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "ref", "_")  # INOUT = PAR
                        currchar = currchar + 1
                    currchar = currchar + 1

            else:
                k = newTemp()
                genquad("+", T_variables[temporary_variables - 1], array_enomeni[currchar + 1], k)
                temporary_variables = temporary_variables + 1

        elif (array_enomeni[currchar] == "-"):
            if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
                currchar = currchar + 1
            if (array_enomeni[currchar + 1] in synartiseis):
                print("BRHKA SYNARTHSH")
                k = newTemp()
                currchar = currchar + 1
                funcname = array_enomeni[currchar]
                genquad("-", T_variables[temporary_variables - 1], funcname, k)
                currchar = currchar + 1  # anoigma parenthesis
                temporary_variables = temporary_variables + 1

                while (array_enomeni[currchar] != ")"):
                    if (array_enomeni[currchar] == "in"):
                        # print("EIMAI STO " + array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "cv", "_")  # IN = CV
                        currchar = currchar + 1
                    if (array_enomeni[currchar] == "inout"):
                        # print("Eimai sto " +array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "ref", "_")  # INOUT = PAR
                        currchar = currchar + 1
                    currchar = currchar + 1
            else:
                k = newTemp()
                genquad("-", T_variables[temporary_variables - 1], array_enomeni[currchar + 1], k)
                temporary_variables = temporary_variables + 1

        elif (array_enomeni[currchar] == "*"):
            if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
                currchar = currchar + 1
            if (array_enomeni[currchar + 1] in synartiseis):
                print("BRHKA SYNARTHSH")
                k = newTemp()
                currchar = currchar + 1
                funcname = array_enomeni[currchar]
                genquad("*", T_variables[temporary_variables - 1], funcname, k)
                currchar = currchar + 1  # anoigma parenthesis]
                temporary_variables = temporary_variables + 1

                while (array_enomeni[currchar] != ")"):
                    if (array_enomeni[currchar] == "in"):
                        # print("EIMAI STO " + array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "cv", "_")  # IN = CV
                        currchar = currchar + 1
                    if (array_enomeni[currchar] == "inout"):
                        # print("Eimai sto " +array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "ref", "_")  # INOUT = PAR
                        currchar = currchar + 1
                    currchar = currchar + 1
            else:
                k = newTemp()
                genquad("*", T_variables[temporary_variables - 1], array_enomeni[currchar + 1], k)
                temporary_variables = temporary_variables + 1

        elif (array_enomeni[currchar] == "/"):
            if (array_enomeni[currchar + 1] == "(" or array_enomeni[currchar + 1] == ")"):
                currchar = currchar + 1
            if (array_enomeni[currchar + 1] in synartiseis):
                print("BRHKA SYNARTHSH")
                k = newTemp()
                currchar = currchar + 1
                funcname = array_enomeni[currchar]
                genquad("/", T_variables[temporary_variables - 1], funcname, k)
                currchar = currchar + 1  # anoigma parenthesis]
                temporary_variables = temporary_variables + 1

                while (array_enomeni[currchar] != ")"):
                    if (array_enomeni[currchar] == "in"):
                        # print("EIMAI STO " + array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "cv", "_")  # IN = CV
                        currchar = currchar + 1
                    if (array_enomeni[currchar] == "inout"):
                        # print("Eimai sto " +array_enomeni[currchar])
                        genquad("par", array_enomeni[currchar + 1], "ref", "_")  # INOUT = PAR
                        currchar = currchar + 1
                    currchar = currchar + 1
            else:
                k = newTemp()
                genquad("/", T_variables[temporary_variables - 1], array_enomeni[currchar + 1], k)
                temporary_variables = temporary_variables + 1


        elif (array_enomeni[currchar] == ";"):
            #print("BGAINO APO TH WHILE THS OPERATIONS " + array_enomeni[currchar])
            break
        currchar = currchar + 1

    genquad(":=", k, "_", array_enomeni[begin])  # BAZO TO TELIKO T STHN METABLHTH THS ISOTHTAS
    # finaloperation()  # APOTHIKEYO TI METABLHTH STON PINAKA SYMBOLON
    #Entity.Variable(array_enomeni[begin])
    #WriteSymbol_Table(array_enomeni[begin], 1)

    # semptyList()

    return currchar


def ASSIGNSTATE(currchar):  # EPISTREFO MIA THESI META TO =
    global declvars
    currchar = currchar - 2
    # print("mpaino assign me metabliti:   " +array_enomeni[currchar])
    varid = array_enomeni[currchar]  # PAIRNO TO ONOMA TIS METABLITIS

    #print(declvars)
    #print(varid)

    if (varid not in declvars):         #BLEPO AN H METABLHTH POY XRHSIMOPOIEITAI EINAI DECLARED
        print("Error variable is not declared", varid)
        #print(declvars)
        exit(-1)

    currchar = currchar + 3  # PIGAINO STIN PRAKSI
    # print("Assign prin to symbolo "+ array_enomeni[currchar])
    if (array_enomeni[currchar + 1] == ";"):  # GIA ISOTHTA ME ENAN ARITHMO PX: X := 5
        temp = array_enomeni[currchar]

        if(Scopeflag ==0 ):
            entity1 = Entity()
            fentity = entity1.Variable(varid)
            scopes[0].add_Entity(fentity)
        elif(Scopeflag == 1 ):
            entity1 = Entity()
            fentity = entity1.Variable(varid)
            scopes[len(scopes)-1].add_Entity(fentity)

        #WriteSymbol_Table(varid, 1)
        # print("EDO " + array_enomeni[currchar])
        genquad(':=', temp, '_', varid)  # EPISTREFEI LISTA
    elif (array_enomeni[currchar + 1] == "("):
        # print("MPIKA CALL")
        currchar = assigncall(currchar)  # DIAXEIRIZETAI KALESMA SYNARTHSHS
    else:
        # print("APO ASSIGN OPERATIONS ME " + array_enomeni[currchar])
        currchar = operations(currchar)

    return currchar


def CALLSTATE(currchar):  # KALESMA XORIS ISOTHTA
    #print("Mpika call me: " + array_enomeni[currchar])
    currchar = currchar + 1  # TO ID THS SYNARTISIS
    funcname = array_enomeni[currchar]
    if (array_enomeni[currchar].isalnum() == True):
        currchar = currchar + 1
        if (array_enomeni[currchar] == "("):
            symbolcheck(currchar)

            while (array_enomeni[currchar] != ";"):
                if (array_enomeni[currchar] == "in"):
                    # print("EIMAI STO " + array_enomeni[currchar])
                    genquad("par", array_enomeni[currchar + 1], "cv", "_")  # IN = CV
                    currchar = currchar + 1
                if (array_enomeni[currchar] == "inout"):
                    # print("Eimai sto " +array_enomeni[currchar])
                    genquad("par", array_enomeni[currchar + 1], "ref", "_")  # INOUT = PAR
                    currchar = currchar + 1
                currchar = currchar + 1
            genquad("call", funcname, "_", "_")

            #print("EIMAI STO " + array_enomeni[currchar])
            if (array_enomeni[currchar] == ";"):
                return currchar
            else:
                print("Error:Missing ; from call statement")
                exit(-1)
        else:
            print("Error:Missing ( in call statement")
            exit(-1)
    else:
        print("Error:Missing ID in call statement")
        exit(-1)

    return currchar


def INPUTSTATE(currchar):  # ELEGXO PARENTHESEIS KAI H EISODOS NA EINAI ALFARITHMITIKO
    # print("INPUT :" +array_enomeni[currchar+2])
    currchar = currchar + 1
    if (array_enomeni[currchar] == "("):
        # print(array_enomeni[currchar])
        symbolcheck(currchar)
        currchar = currchar + 1

        if (array_enomeni[currchar].isalnum()):
            print("INPUT: " + array_enomeni[currchar])
            return

        else:
            print("Error:Wrong input")
            exit(-1)
    else:
        print("Error: Missing ( from input")
        exit(-1)
    return


def PRINTSTATE(currchar):  # BLEPO AN YPARXEI PARENTHESI,AN KLEINEI KAI AN META TO KLEISIMO EXEI ;
    if (array_enomeni[currchar + 1] == "("):

        symbolcheck(currchar + 1)

        #print("PRINT:" + array_enomeni[currchar + 2])
        return
    elif (array_enomeni[currchar + 1] != "("):
        print("Error couldnt find '(' after print")
        exit(-1)


def STATEMENTS(currchar):  # STATEMENTS MEXRI PARENTHESI
    while (array_enomeni[currchar] != "}"):
        if (array_enomeni[currchar] == "program" or array_enomeni[currchar] == "default" or array_enomeni[
            currchar] == "or" or array_enomeni[currchar] == "and" or array_enomeni[currchar] == "not"
                or array_enomeni[currchar] == "function" or array_enomeni[currchar] == "procedure" or array_enomeni[
                    currchar] == "in" or array_enomeni[currchar] == "inout"):
            print("Error: forbidden word : " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "if"):
            currchar = IFSTATE(currchar)
        elif (array_enomeni[currchar] == "else"):
            print("Error:You should insert if statement before else: ")
            exit(-1)
        elif (array_enomeni[currchar] == "while"):  # TO WHILE EPISTREFEI MIA THESI META TO } TOY
            # print("MPAINO STI WHILE ME : " + array_enomeni[currchar])
            currchar = WHILESTATE(currchar)
            # print("Bgaino apo while me: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "switchcase"):
            currchar = SWITCHSTATE(currchar)
        elif (array_enomeni[currchar] == "forcase"):
            currchar = FORCASESTATE(currchar)
            # print("BGAINO APO FOR ME: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "incase"):
            currchar = INCASE(currchar)
            # print("BGAINO APO INCASE ME:  " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "call"):
            currchar = CALLSTATE(currchar)
        elif (array_enomeni[currchar] == "input"):
            INPUTSTATE(currchar)
        elif (array_enomeni[currchar] == "print"):
            PRINTSTATE(currchar)
        elif (array_enomeni[currchar] == "="):
            print("Error Missing ':' before '=': " + array_enomeni[currchar - 1])
            exit(-1)

        elif (array_enomeni[currchar] == "return"):
             genquad("retv", array_enomeni[currchar + 1], "_", "_")

        elif (array_enomeni[currchar] == ":"):
            currchar = currchar + 1

            if (array_enomeni[currchar] == "="):
                # print("MPAINO ASSIGN")
                currchar = ASSIGNSTATE(currchar)
                # print("Bgaino apo assign me ", array_enomeni[currchar])
            else:
                print("Error : missing '=' in variable: " + array_enomeni[currchar - 2])
                exit(-1)
        currchar = currchar + 1
    return currchar


def DEFAULTSTATEMENTS(currchar):  # STATEMENTS MEXRI EROTIMATIKO
    while (array_enomeni[currchar] != ";"):
        if (array_enomeni[currchar] == "program" or array_enomeni[currchar] == "default" or array_enomeni[
            currchar] == "or" or array_enomeni[currchar] == "and" or array_enomeni[currchar] == "not"
                or array_enomeni[currchar] == "function" or array_enomeni[currchar] == "procedure" or array_enomeni[
                    currchar] == "in" or array_enomeni[currchar] == "inout"):
            print("Error: forbidden word : " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "if"):
            currchar = IFSTATE(currchar)
        elif (array_enomeni[currchar] == "else"):
            print("Error:You should insert if statement before else: ")
            exit(-1)
        elif (array_enomeni[currchar] == "while"):  # TO WHILE EPISTREFEI MIA THESI META TO } TOY
            # print("MPAINO STI WHILE ME : " + array_enomeni[currchar])
            currchar = WHILESTATE(currchar)
            # print("Bgaino apo while me: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "switchcase"):
            currchar = SWITCHSTATE(currchar)
        elif (array_enomeni[currchar] == "forcase"):
            currchar = FORCASESTATE(currchar)
            # print("BGAINO APO FOR ME: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "incase"):
            currchar = INCASE(currchar)
            # print("BGAINO APO INCASE ME:  " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "call"):
            currchar = CALLSTATE(currchar)
        elif (array_enomeni[currchar] == "input"):
            INPUTSTATE(currchar)
        elif (array_enomeni[currchar] == "print"):
            PRINTSTATE(currchar)
        elif (array_enomeni[currchar] == "="):
            print("Error Missing ':' before '=': " + array_enomeni[currchar - 1])
            exit(-1)
        elif (array_enomeni[currchar] == ":"):
            currchar = currchar + 1
            if (array_enomeni[currchar] == "="):
                # print("MPAINO ASSIGN")
                currchar = ASSIGNSTATE(currchar)
                # print("Bgaino apo assign me ", array_enomeni[currchar])
            else:
                print("Error : missing '=' in variable: " + array_enomeni[currchar - 2])
                exit(-1)
        currchar = currchar + 1
    return currchar


def CASESTATEMENTS(currchar):  # STATEMENTS MEXTI PARENTHESI )
    while (array_enomeni[currchar] != "default"):
        if (array_enomeni[currchar] == "program" or array_enomeni[currchar] == "default" or array_enomeni[
            currchar] == "or" or array_enomeni[currchar] == "and" or array_enomeni[currchar] == "not"
                or array_enomeni[currchar] == "function" or array_enomeni[currchar] == "procedure" or array_enomeni[
                    currchar] == "in" or array_enomeni[currchar] == "inout"):
            print("Error: forbidden word : " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "if"):
            currchar = IFSTATE(currchar)
        elif (array_enomeni[currchar] == "else"):
            print("Error:You should insert if statement before else: ")
            exit(-1)
        elif (array_enomeni[currchar] == "while"):  # TO WHILE EPISTREFEI MIA THESI META TO } TOY
            # print("MPAINO STI WHILE ME : " + array_enomeni[currchar])
            currchar = WHILESTATE(currchar)
            # print("Bgaino apo while me: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "switchcase"):
            currchar = SWITCHSTATE(currchar)
        elif (array_enomeni[currchar] == "forcase"):
            currchar = FORCASESTATE(currchar)
            # print("BGAINO APO FOR ME: " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "incase"):
            currchar = INCASE(currchar)
            # print("BGAINO APO INCASE ME:  " + array_enomeni[currchar])
        elif (array_enomeni[currchar] == "call"):
            currchar = CALLSTATE(currchar)
        elif (array_enomeni[currchar] == "input"):
            INPUTSTATE(currchar)
        elif (array_enomeni[currchar] == "print"):
            PRINTSTATE(currchar)
        elif (array_enomeni[currchar] == "="):
            print("Error Missing ':' before '=': " + array_enomeni[currchar - 1])
            exit(-1)
        elif (array_enomeni[currchar] == ":"):
            currchar = currchar + 1
            if (array_enomeni[currchar] == "="):
                print("MPAINO ASSIGN")
                currchar = ASSIGNSTATE(currchar)
                print("Bgaino apo assign me ", array_enomeni[currchar])
            else:
                print("Error : missing '=' in variable: " + array_enomeni[currchar - 2])
                exit(-1)
        currchar = currchar + 1
    return currchar


def CFILE():
    # Open files to write
    # intFile = open('intFile.int', 'w')
    cFile = open('CFile.c', 'w')

    cFile.write("int main( ){   \n\t")
    # print("EIMAI  STH CFILE")
    cFile.write("\n")
    cFile.write("int ")
    for i in declvars:
        cFile.write("%s, " % i)
    for i in T_variables:
        cFile.write("%s, " % i)
    cFile.write(";")

    cFile.write("\n \n")

    i = 0
    for i in range(len(quad_list)):
        if (quad_list[i][1] == 'begin_program'):
            cFile.write("L_" + str(i + 1) + "\t" + quad_list[i][2] + ":\n\t")

        if (quad_list[i][1] == "begin_function" or quad_list[i][1] == "begin_procedure"):
            cFile.write("L_" + str(i + 1) + "\t" + quad_list[i][2] + ":\n\t")


        elif (quad_list[i][1] == "-"):
            cFile.write(
                "L_" + str(i + 1) + ": " + quad_list[i][4] + "=" + quad_list[i][2] + "-" + quad_list[i][3] + ";\n\t")

        elif (quad_list[i][1] == "+"):
            cFile.write(
                "L_" + str(i + 1) + ": " + quad_list[i][4] + "=" + quad_list[i][2] + "+" + quad_list[i][3] + ";\n\t")

        elif (quad_list[i][1] == "/"):
            cFile.write(
                "L_" + str(i + 1) + ": " + quad_list[i][4] + "=" + quad_list[i][2] + "/" + quad_list[i][3] + ";\n\t")

        elif (quad_list[i][1] == "*"):
            cFile.write(
                "L_" + str(i + 1) + ": " + quad_list[i][4] + "=" + quad_list[i][2] + "*" + quad_list[i][3] + ";\n\t")

        elif (quad_list[i][1] == ":="):
            cFile.write("L_" + str(i + 1) + ": " + quad_list[i][4] + "=" + quad_list[i][2] + ";\n\t")

        elif (quad_list[i][1] == "jump"):
            cFile.write("L_" + str(i + 1) + ": " + "" + "goto L_" + str(quad_list[i][4]) + ";\n\t")

        elif (quad_list[i][1] == "="):
            cFile.write("L_" + str(i + 1) + ": " + "if(" + quad_list[i][2] + "==" + quad_list[i][3] + ") goto L_" + str(
                quad_list[i][4] + 1) + ";\n\t")

        elif (quad_list[i][1] == "<"):
            cFile.write("L_" + str(i + 1) + ": " + "if(" + quad_list[i][2] + "<" + quad_list[i][3] + ") goto L_" + str(
                quad_list[i][4] + 1) + ";\n\t")

        elif (quad_list[i][1] == "<="):
            cFile.write("L_" + str(i + 1) + ": " + "if(" + quad_list[i][2] + "<=" + quad_list[i][3] + ") goto L_" + str(
                quad_list[i][4] + 1) + ";\n\t")

        elif (quad_list[i][1] == ">"):
            cFile.write("L_" + str(i + 1) + ": " + "if(" + quad_list[i][2] + ">" + quad_list[i][3] + ") goto L_" + str(
                quad_list[i][4] + 1) + ";\n\t")

        elif (quad_list[i][1] == ">="):
            cFile.write("L_" + str(i + 1) + ": " + "if(" + quad_list[i][2] + ">=" + quad_list[i][3] + ") goto L_" + str(
                quad_list[i][4] + 1) + ";\n\t")

        elif (quad_list[i][1] == "<>"):
            cFile.write("L_" + str(i + 1) + ": " + "if(" + str(quad_list[i][2]) + "!=" + str(
                quad_list[i][3]) + ") goto L_" + str(quad_list[i][4] + 1) + ";\n\t")


        elif (quad_list[i][1] == "end_function" or quad_list[i][
            1] == "end_procedure"):  # print to apotelesma tou expression.
            cFile.write("L_" + str(i + 1) + "" + "\t" + "end of block: " + str(quad_list[i][2]) + ";\n\t")


        elif (quad_list[i][1] == "end_program"):  # print to apotelesma tou expression.
            cFile.write("L_" + str(i + 1) + " " + "end of program: " + str(quad_list[i][2]) + ";\n\t")
    # cCode(cFile)

    cFile.write("\n   }")

    cFile.close()


def INTFILE():
    global declvars
    intFile = open('iFile.int', 'w')
    intFile.write("\n")
    for i in quad_list:
        intFile.write("%s, " % i)
        intFile.write("\n")

    intFile.close()



# ---------  SYNARTHSEIS ENDIAMESOU KODIKA   ---------

global Quad_list
global quad_count
global T_variables
global T_i
T_i = 1
quad_list = []  # Lista apo tis tetrades pou ftiaxno
quad_counter = 0  # Arithmos tetradas pou
T_variables = []  # Lista apo tis temporary metablites pou ftiaxno

tempcounter = 0


def nextquad():  # Tha tin kalo gia na proxoriso stin epomeni tetrada
    global quad_counter
    return quad_counter


def genquad(op, x1, x2, z):                     # dimiourgei tetrada me op ,x1,x2,z
    global quad_list
    global quad_counter
    list = []

    list = [nextquad()]                                 # Bazo ton arithmo tis  tetradas

    list += [op] + [x1] + [x2] + [z]

    quad_counter += 1                           # Pigaino sthn epomeni tetrada
    quad_list += [list]                             # Prostheto tin tetrada sto synolo tetradon
    return list


def newTemp():
    global T_i
    global T_variables

    localList = ['T_']
    localList.append(str(T_i))
    temporaryVariable = " ".join(localList)

    T_i += 1  # STO EPOMENO KALESMA THA ALLAKSEI I TOPIKI

    T_variables += [temporaryVariable]
    if (Scopeflag == 0):
        entity1 = Entity()
        fentity = entity1.Temporary_Variable(temporaryVariable)
        scopes[0].add_Entity(fentity)

    elif (Scopeflag == 1):
        entity1 = Entity()
        fentity = entity1.Temporary_Variable(temporaryVariable)
        scopes[len(scopes) - 1].add_Entity(fentity)

    return temporaryVariable


def finaloperation():  # MOLIS TELEIOSOUN OI PRAKSEIS ATHRIZEI TIS TEMPORARY METABLITES !!PROSOXI ASTO GIA TELIKO KODIKA
    print("EDO THA  GINEI H TELIKI PRAKSI ME PROSTHESI THS T_Variables KAI TO ADEIASMA THS")

    T_variables = []




def emptyList():  # dimiourgei lista apo pointers

    list_of_pointers = []  # Arxikopoihsh pointer list.

    return list_of_pointers


def makeList(x):  # Lista etiketon me mono to X mesa

    X_list = [x]  # PROSOXI !! Den ksero pou tha to xrisimopoiso akoma

    return X_list


def merge(list_1, list_2):  # Dimiourgei lista apo etiketes enonontas 2 listes

    tag_list = []
    tag_list += list_1 + list_2

    return tag_list


def backPatch(tag_list, z):  # Gia kathe tetrada apo to quad_list kano to teleytaio psifio z

    global quad_list
    # print("MPAINO BACKPATCH")
    #print("TAG LIST PRIN " + tag_list[4])
    tag_list[4] = z  # kano stin kathe tetrda to teleytaio psifio z

    #print("PRINT TAG LIST ALLGMENH" + str(tag_list[4]))
    return


# --------------------------------------------------------------------------------

# ---------- PINAKAS SYMBOLWN ----------

global scopes
scopes = []
global offset
offset = 8


def Write_Symbol_Table():  # TYPES : 0 FOR SCOPE , 1 FOR ENTITIES , 2 FOR ARGUMENTS
  Symbol_Table = open("Symbol_Array.txt", 'a')

  for i in scopes:
      Symbol_Table.write("\n")
      Symbol_Table.write("Scope" +str(i.nestingLevel))

      for j in i.entityList :
         Symbol_Table.write(" ---> ")
         Symbol_Table.write(j.name)
         Symbol_Table.write("/")
         Symbol_Table.write(str(j.offset))

  Symbol_Table.close()

def computeOffset():
    global offset
    offset = offset + 4
    return offset


def deleteOffset():
    global offset
    offset = 8
    return offset


class Scope():
    global scopes
    arguments = []

    def __init__(self, Level, offset):
        self.entityList = []
        self.nestingLevel = Level
        self.offset = 8



    def add_Scope(name):
        scopes.append(name)

    def add_Entity(self, Entity):
        self.entityList.append(Entity)

    def delete_Scope(self, name):
        scopes.remove(name)


class Entity():

    def __init__(self):
        self.name = ""
        self.type = "Int"


    class Variable:

        def __init__(self, name):
            self.name = name
            self.type = "Int"
            self.offset = computeOffset()

        def retName(self):
            return self.name
    class SubProgram:

        def __init__(self, name, type, startquad, listargument,
                   listframelength):  # Start quad to quad pou ksekinao kai listframelength mikos eggrafimatos
            self.name = name
            self.type = type
            self.startquad = startquad
            self.listargument = listargument
            self.offset = computeOffset()

        def retName(self):
            return self.name



    class Const:

        def __init__(self, name, value):
            self.name = name
            self.value = value

            def retName(self):
                return self.name

    class Parameter:
        def __init__(self, name, offset):
            self.name = name
            self.parMode = []
            self.offset = computeOffset()

        def retName(self):
            return self.name

    class Temporary_Variable:

        def __init__(self, name):
            self.name = name
            self.type = "Int"
            self.offset = computeOffset()

        def retName(self):
            return self.name


class Argument:
    def __init__(self, parMode, type):
        self.parMode = parMode
        self.type = type

global rnumber
rnumber =0
global assFile

def final():
    global Quad_list
    global rnumber
    global assFile
    p=0
    assFile=open("assemblyFile.asm", 'w')
    assFile.write("\n")
    for i in range(len(quad_list)):
        if (quad_list[i][1] == 'jump'):
            assFile.write('b' + ' ' + str(quad_list[i][4]) + '\n')

        if (quad_list[i][1] == ':='):

            loadvr(quad_list[i][2], rnumber)

            storerv(rnumber, quad_list[i][4])
            rnumber = rnumber + 1



        if (quad_list[i][1] == '+'):
            Flag =1
            loadvr(quad_list[i][2],"$t1")
            loadvr(quad_list[i][3],"$t2")
            Flag=0
            assFile.write('add,$t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])

        elif(quad_list[i][1] == '-'):
            Flag = 1
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            Flag = 0
            assFile.write('sub,$t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])

        elif(quad_list[i][1] == '*'):
            Flag = 1
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            Flag = 0
            assFile.write('mul,$t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])


        elif(quad_list[i][1] == '/'):
            Flag = 1
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            Flag = 0
            assFile.write('div,$t1,$t1,$t2' + '\n')
            storerv(1, quad_list[i][4])



        if (quad_list[i][1] == '<>'):
            loadvr(quad_list[i][2],"$t1")
            loadvr(quad_list[i][3],"$t2")
            assFile.write('bne,$t1,$t2,' + str(quad_list[i][4]) + '\n')

        elif(quad_list[i][1] == '>'):
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            assFile.write('bgt,$t1,$t2,' + str(quad_list[i][4]) + '\n')

        elif (quad_list[i][1] == '<'):
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            assFile.write('blt,$t1,$t2,' + str(quad_list[i][4]) + '\n')
        elif(quad_list[i][1] == '>='):
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            assFile.write('bge,$t1,$t2,' + str(quad_list[i][4]) + '\n')

        elif (quad_list[i][1] == '<='):
            loadvr(quad_list[i][2], "$t1")
            loadvr(quad_list[i][3], "$t2")
            assFile.write('ble,$t1,$t2,' + str(quad_list[i][4]) + '\n')

        elif(quad_list[i][1]=="retv"):
            loadvr(quad_list[i][2], "$t1")
            storerv("$t1",quad_list[i][2])



def searchentity(name):
    global scopes
    #print("EIMAI EDO ",name)
    for i in scopes:

        for j in i.entityList:
            if(j.retName() == name):
                #print("EIMAI EDO ", j)
                return j


def gnlv(name):
    global assFile
    entvar = searchentity(name)
    assFile.write("lw $t0,-4($sp)")
    assFile.write("\n")
    assFile.write("addi $t0,$t0,-", entvar.offset, "\n")



    assFile.write("\n")

def loadvr(v,r):
     #entvar = searchentity(v)
     #y = entvar.offset
     #assFile.write('li $t%d,%s\n' % (r, y ))


     if (v.isdigit()==True):  # If variable is constant.
         assFile.write("li $t" + str(r) + "," + str(v) + "\n")
         return


def storerv(r,v):
    #if (v not in declvars and ):
        #print("This variable is not declared ", v)
        #exit(-1)

    if(v.isalpha() ==True ):
        #print("EIAMAI EFO ", v)

        entvar = searchentity(v)
        #print(entvar)
        assFile.write("sw $t"+str(r) + ",-" + str(entvar.offset) + "($s0)\n")


YACC()  
#CFILE()
