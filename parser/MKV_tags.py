import re


def getMkvTagVal(chunk):

    #decoding into english (from binary) to run regex commands on the chunk/metadata
    chunk_en = chunk.decode('cp437')

    match = re.search("AWS_KINESISVIDEO_FRAGMENT_NUMBERD", chunk_en)
    if(match):
        fragment_nbr_chunk = re.split("AWS_KINESISVIDEO_FRAGMENT_NUMBERD", chunk_en)



    val = fragment_nbr_chunk[1]

    print("AWS_KINESISVIDEO_FRAGMENT_NUMBER -->   ",val[val.find("ç")+1:val.find("g")])
    print("")


    match1 = re.search("AWS_KINESISVIDEO_SERVER_TIMESTAMPD", val)
    if(match1):
        server_time_chunk = re.split("AWS_KINESISVIDEO_SERVER_TIMESTAMPD", val)

    nextval =server_time_chunk[1]



    print("AWS_KINESISVIDEO_SERVER_TIMESTAMP -->   ",nextval[nextval.find("ç")+1:nextval.find("g")])
    print("")


    match2 = re.search("AWS_KINESISVIDEO_PRODUCER_TIMESTAMPD", nextval)
    if(match2):
        producer_time_chunk = re.split("AWS_KINESISVIDEO_PRODUCER_TIMESTAMPD", nextval)



    nextval2 =producer_time_chunk[1]


    print("AWS_KINESISVIDEO_PRODUCER_TIMESTAMP -->   ",nextval2[nextval2.find("ç")+1:nextval2.find("C")])
    print("")
    #codecs.register_error('slashescape', slashescape)