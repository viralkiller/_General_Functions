import re
import random
import string
import xmltodict
import xml.etree.ElementTree as ET
import json

class txt_Ops():

    def __init__(self):
        pass

  ########################################################################################

    #converts a XML file to a python dictionary, leave define_root as blank '' in most cases...
    def xml_To_Dict(self,filename,define_root):
        data_dict = {}
        tree = ET.parse(filename)
        xml_data = tree.getroot()
        xmlstr = ET.tostring(xml_data,encoding='utf-8',method='xml')
        if define_root == '':
            data_dict = dict(xmltodict.parse(xmlstr))
        else:
            data_dict = dict(xmltodict.parse(xmlstr)[define_root])
        return data_dict




    def illegal_Char_Replacer_Email(self,input_string):

        #print(input_string)

        #input_string = re.sub(r"[a-zA-Z0-9 .@]","",input_string)
        #input_string = input_string.lower()

        #print(input_string)
        return input_string

    def illegal_Char_Replacer(self,input_string):

        print(input_string)

        input_string = input_string.replace("%","((oo))")
        input_string = input_string.replace("?","((ss))")
        input_string = input_string.replace(",","((vv))")
        input_string = input_string.replace("$","((dd))")
        input_string = input_string.replace("/","((ll))")
        input_string = input_string.replace("+","((tt))")
        input_string = input_string.replace("£","((rr))")
        input_string = input_string.replace("=","((ee))")
        input_string = input_string.replace("!","((xx))")
        input_string = input_string.replace("*","((os))")
        input_string = input_string.replace("&","((aa))")
        input_string = input_string.replace('"',"((ttt))")
        input_string = input_string.replace('|',"((lll))")
        input_string = input_string.replace('#',"((hhh))")
        input_string = re.sub(r"[^a-zA-Z0-9 '_():!-{}][.]","▓",input_string)
        #input_string = re.sub(r"[^a-zA-Z0-9 '._():!-{}£[]","",input_string)
        print(input_string)
        return input_string

    def illegal_Char_Decoder(self,input_string):
        input_string = input_string.replace("((oo))","%")
        input_string = input_string.replace("((ss))","?")
        input_string = input_string.replace("((vv))",",")
        input_string = input_string.replace("((dd))","$")
        input_string = input_string.replace("((ll))","/")
        input_string = input_string.replace("((tt))","+")
        input_string = input_string.replace("((rr))","£")
        input_string = input_string.replace("((ee))","=")
        input_string = input_string.replace("((xx))","!")
        input_string = input_string.replace("((os))","*")
        input_string = input_string.replace("((aa))","&")
        input_string = input_string.replace("((ttt))",'"')
        input_string = input_string.replace("((lll))","|")
        input_string = input_string.replace("((hhh))","#")
        return input_string



    def quick_read_txt_file(self,file_path):
        with open (file_path, "r") as f:
            input_str=str(f.readlines())
        input_str=input_str[2:-2]
        return input_str

    def quick_write_txt_file(self,file_path,val_to_write):
        with open(file_path, "w+") as myfile:
            myfile.write( str(val_to_write)  )
            myfile.close()

    def quick_append_txt_file(self,file_path,val_to_write):
        with open(file_path, "a") as myfile:
            myfile.write( str(val_to_write)  )
            myfile.close()

  ########################################################################################

    def line_Replacer(self,filename,line_num,content):
        with open (filename, "r") as f:
            get_all=f.readlines()
        with open(filename,'w') as f:
            for i,line in enumerate(get_all,1):
                if i==line_num:
                    f.writelines(content)
                else:
                    f.writelines(line)

    def replace_Specific_Line(self,filename,line_number,line_content):
        with open (filename, "r") as f:
            get_all=f.readlines()
        with open(filename,'w') as f:
            for i,line in enumerate(get_all,1):
                if i==int(line_number):
                    f.writelines(str(line_content))
                else:
                    f.writelines(line)
        print("\nLine:",line_number,"has been replaced with:",line_content,'\n')

  #----------------------------------------------------------------------------------------



    def split_String_At(self,input_string,split_symbol):
        string_array = []
        if input_string.find(split_symbol) > 0:
            string_array = input_string.split(split_symbol)
        else:
            print("\nError: Input string contains no",split_symbol,"character...")
        return string_array


    def find_Digit_Before_Dot(self,input_float):
        input_str = str(input_float)
        for i in range(len(input_str)):
            if input_str[i] == '.':
                print("\nFound a dot:",input_str[i-1]+input_str[i],"\n")
                return input_str[i-1]

    def read_commas_into_array(self,file_path):
        results_array = []
        counter = 0
        in_file = open(file_path,'r')
        for line in in_file:
            for value in line.strip().split(','):
                counter += 1
                results_array.append(value)
        return results_array

    def create_dict_from_txt(self,file_path,split_symbol):
        #assumes dict values are on separate lines
        parts=[]
        dictionary={}
        with open (file_path, "r") as hfile:
            sp = hfile.read()
        lines = sp.split("\n")
        for line in lines:
            if line!='':
                parts = line.split(split_symbol)
            dictionary[parts[0]]=parts[1]
        return dictionary

    def find_All_Numbers_Dots(self,source_string):
        #good for scraping floats
        new_str=''
        get_digits = re.findall(r"([0-9.]*[0-9]+)",source_string)
        for i in range( len(get_digits) ):
            new_str=new_str+str(get_digits[i])
        final_val = float(new_str)
        return final_val

######## SPECIAL ########################################################################################

    def make_Unique_From_Email(self,input_string):
        illegal_chars = [".",",","?","#","[","]","{","}","(",")","%","$","£","'",'"',"+","<",">"]
        unique_code = ''
        unique_number = random.randrange(1,9)
        split_email = self.split_String_At(input_string,'@')
        unique_code = split_email[0] + '_' + split_email[1][0] + str(unique_number)
        for i in range( len(illegal_chars) ):
            unique_code = unique_code.replace(illegal_chars[i],"_")
        unique_code = unique_code.lower()
        return unique_code


    def txt_total_comma_values(self,file_path):
        in_file = open(file_path, 'r')
        for line in in_file:
            float_counter = 0
            for num in line.strip().split(','):
                float_counter += float(num)
            floats_total = ("%d\n" % float_counter)
        return floats_total


    def array_String_To_Array(self,input_string):
        input_string = input_string.replace("'","")
        input_string = input_string[1:-1]
        print(input_string)
        filter_array = []
        for val in input_string.strip().split(','):
            #lstrip takes away leading spaces
            filter_array.append(val.lstrip())
        return filter_array


    def find_Chars_Before_Symbol(self,input_str,symbol_to_find,how_may_chars):

        for i in range(len(input_str)):

            if input_str[i] == symbol_to_find:

                return_str = input_str[(i-how_may_chars):i]

                #print("\nFound char:",symbol_to_find,"| Previous",how_may_chars,"chars:",return_str,"\n")

                return return_str




#check class
def check_Module():

    txt_ops = txt_Ops()


    #a = txt_ops.array_String_To_Array("['hello','  Sir Madam Betty','  how','  are','  you']")
    #print(a[0],'|',a[1],'|',a[2],'|',a[3])

    b = txt_ops.illegal_Char_Replacer("***Best --Friend's NFT!!!?%%$$$")
    print(b)

    c = txt_ops.illegal_Char_Decoder(b)
    print(c)
    #b = txt_ops.illegal_Char_Replacer("(best_type...)")
    #print(b)
    #b = txt_ops.read_commas_into_array('static/txt/description/countries/733760db-76ec-4736-bf13-939e2e84264c.txt')
    #print(b)

if __name__==('__main__'):
    check_Module()



