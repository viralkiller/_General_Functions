import csv




class csv_Ops():


    def __init__(self):

        self.object_ID = self
        #print(self.object_ID)


    def csv_Count_Cols(self,filename):
        with open(filename, 'r') as csv:
            first_line = csv.readline()
            #your_data = csv.readlines()
        ncol = first_line.count(',') + 1
        return ncol






    def append_to_CSV(self,file_name,row_array):

        data_row = [row_array]

        myFile = open(file_name,'a',newline='')

        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(data_row)

        myFile.close()

        #print("\nData row appended to CSV file",file_name)





    def write_to_CSV(self,file_name,row_array):

        data_row = [row_array]

        myFile = open(file_name,'w',newline='')

        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(data_row)

        myFile.close()

        #print("\nData row written (destructive) to CSV file",file_name)








    def read_Last_CSV_Rows(self,file_name,limit):

        results_array = []

        #input variable str processing - convert line to int
        limit = int(str(limit).replace('limit=',''))

        with open(file_name, 'r') as f:

            read_list = list(csv.reader(f))[-int(limit-1)-1:]

            #print("\nread_list:",read_list)

            row_length = len(read_list)

            #print("\nrow_length:",row_length)

            for row in read_list:

                #print(row)



                if row != [''] and row != [] and row != '' and len(row) > 0:

                    #print(row)

                    data = ', '.join(row)

                    row = [x.strip() for x in data.split(',')]

                    #print("\nRequested row:",row)

                    results_array.append(row)

            #example use
            #last_row = csv_ops.read_Last_CSV_Rows('csv/whales.csv','limit=5')

            #print("\nget last rows,results_array",results_array,len(results_array))

            f.close()

        return results_array






    def match_Last_CSV_Rows(self,file_name,match_col,find_val,return_col,limit):

        #uses 0,1,2 indexing from zero

        status = ''
        return_val = '' #if '' is returned nothing was matched

        #string clean-up ops
        limit = int(str(limit).replace('limit=',''))
        match_col = int(str(match_col).replace('match_col=',''))
        return_col = int(str(return_col).replace('return_col=',''))
        find_val = str(find_val).replace('find_val=','')

        get_rows = self.read_Last_CSV_Rows(file_name,limit)

        #print("\nget_rows:",get_rows)

        get_rows_length = len(get_rows)

        print("\nScanning",limit,"rows for value:",find_val)

        for i in range(get_rows_length):

            #print("\nget_rows[i]",get_rows[i],len(get_rows[i]))

            if get_rows[i] != '' and get_rows[i] != [''] and get_rows[i] != [] and len(get_rows[i]) > 1:

                search_val = get_rows[i][match_col]

                #print("get_rows[i]",get_rows[i])

                if search_val == find_val:

                    status = 'MATCH'

                    return_val = get_rows[i][return_col]

                    #print("\nRow",str(i+1),"|",search_val,"| MATCH FOUND | Return value:",return_val)

                else:

                    status = 'NO_MATCH'

                    #print("\nRow",str(i+1),"|",search_val,"|",status)

        #example use:
        #match_row = csv_ops.match_Last_CSV_Rows('csv/whales.csv','match_col=2','find_val=3880158.0','return_col=0','limit=8')

        return status,return_val














def check_Module():

    csv_ops = csv_Ops()

    #a = csv_ops.write_to_CSV('csv/test.csv', [1,2,3] )
    #print('a:',a)

    #b = csv_ops.append_to_CSV('csv/test.csv', [4,5,6] )
    #print('b:',b)

    c = csv_ops.csv_Count_Cols('db/intent_to_sell.csv')
    print('\nCol count:',c)





if __name__ == '__main__':

    check_Module()


