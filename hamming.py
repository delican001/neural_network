import math

msglen = 32 + 26



def msg2bin(msg, bin_len):
    bin_msg = ''.join(format(ord(x), 'b') for x in msg)
    ans = []
    while len(bin_msg) > 0:
        if len(bin_msg) < bin_len:
            ans.append(bin_msg)
            bin_msg = ''
        else:
            ans.append(bin_msg[:bin_len])
            bin_msg = bin_msg[bin_len:]
    return ans


def insert_empty(msg_, position):
    if position!=0:
        left = msg_[:position - 1]
        right = msg_[position - 1:]
        temp = left + '0' + right
    else:
        temp = '0' + msg_
    return temp


def insert_bit(msg_, position, bit):
    if position == msg_.__len__():
        tmp = msg_[0:len(msg_) - 1] + bit
    elif position ==0:
        tmp = bit + msg_[1:]
    elif position ==1:
        tmp = msg_[0] + bit + msg_ [2:]
    else:
        left = msg_[0:position]
        right = msg_[position+1:]
        tmp = left + bit + right
    return tmp

def add_sum_bit(msg):
    sum=0
    for l in msg:
        sum=sum+int(l)
    res = msg+str(sum%2)
    return res


def encrypt(mesg):
    msg_=mesg
    i = 1
    bit_nums = []
    while i <= len(msg_):
        bit_nums.append(i)
        i = i * 2
    for k in bit_nums:
        msg_ = insert_empty(msg_, k)
    sums=[]
    for k in range(bit_nums.__len__()):
        num = bit_nums[k] - 1
        sum = 0
        while num < len(msg_):
            if (bit_nums[k] - 1 != 0):
                for q in range(bit_nums[k]):
                    sum = sum + int(msg_[num])
                    num = num + 1
                    if (num == msg_.__len__()):
                        break
                num = num - 1
                if (num-1 == msg_.__len__()):
                    break
            else:
                sum = sum + int(msg_[num])
            num = num + bit_nums[k] + 1
        sums.append(sum % 2)
    for k in range(bit_nums.__len__()):
        msg_ = insert_bit(msg_, bit_nums[k]-1, str(sums[k]))
    msg_ = add_sum_bit(msg_)
    return msg_

def check_control_bits(msg):
    msg_,deleted_=delete_control(msg)
    encrypted = encrypt(msg_)
    msg__ , deleted__ = delete_control(encrypted)
    sum=0
    for i in range(deleted_.__len__()):
        if deleted_[i]!=deleted__[i]:
            sum=sum+int(math.pow(2,i))
    return sum


def delete_control(msg):
    bit_nums=[]
    i=1
    while i < len(msg):
        bit_nums.append(i-1)
        i=i*2
    res=""
    for i in range(len(msg)):
        if i in bit_nums:
            pass
        else:
            res=res+msg[i]
    deleted=""
    for i in range(bit_nums.__len__()):
        deleted=deleted+msg[bit_nums[i]]
    return res,deleted


def decode(msg):
    sum=0
    bit_nums=[]
    i=1
    while i < len(msg):
        bit_nums.append(i-1)
        i=i*2
    for i in range(len(msg)-1):
        sum=sum+int(msg[i])
    ok = sum%2==int(msg[len(msg)-1])
    print(ok)
    control = check_control_bits(msg)
    print(control)
    if (control==0) and ok:
        return delete_control(msg)[0]
    elif (control==0)==ok:
        if msg[control-1]=='0':
            msg = insert_bit(msg,control-1,'1')
        else:
            msg = insert_bit(msg, control-1, '0')
        return delete_control(msg)[0]
    else:
        raise AssertionError ("SOME SHIT HAPPEN")

if __name__ == '__main__':
    messages = msg2bin("hello", 7)
    habr_test=[]
    habr_test.append("0100010000111101")
    habr_test.append("0011111001001000")
    new_messages=[]
    for message in messages:
        new_messages.append(encrypt(message))
    try:
        print(decode(insert_bit(insert_bit(new_messages[0],5,'1'),3,'1')))
    except AssertionError as exc:
        print(type(exc))
        print(exc.args)

    print(messages[0])