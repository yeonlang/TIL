def isanswer(answer, letters):
    if ''.join(letters)==answer:
        return True
    else :
        return False
        
def status(answer, letters, lst):
    for j,k in enumerate(answer):
        if k in letters:
            lst[j]=k
    return lst

def call(a=''):
    import random
    lst2=['according,',
    'account',
    'actually',
    'add',
    'address',
    'administration',
    'against',
    'agency',
    'agreement',
    'ahead',
    'although',
    'always',
    'American',
    'animal',
    'another',
    'answer',
    'around',
    'arrive',
    'article',
    'artist',
    'author',
    'authority',
    'available',
    'beautiful',
    'because',
    'behavior',
    'behind',
    'believe',
    'better',
    'between',
    'beyond',
    'building',
    'business',
    'campaign',
    'candidate',
    'capital',
    'central',
    'century',
    'certain',
    'certainly',
    'chance',
    'change',
    'character',
    'church',
    'citizen',
    'collection',
    'commercial',
    'community',
    'company',
    'compare',
    'computer',
    'concern',
    'condition',
    'conference',
    'create',
    'crime',
    'cultural',
    'culture',
    'decade',
    'decide',
    'decision',
    'Democrat',
    'democratic',
    'describe',
    'design',
    'despite',
    'difference',
    'different',
    'difficult',
    'director',
    'discover',
    'discuss',
    'economic',
    'economy',
    'education',
    'employee',
    'especially',
    'establish',
    'everybody',
    'everyone',
    'everything',
    'evidence',
    'exactly',
    'example',
    'executive',
    'generation',
    'government',
    'great',
    'green',
    'ground',
    'group',
    'grow',
    'growth',
    'guess',
    'however',
    'huge',
    'human',
    'hundred',
    'husband',
    'include',
    'including',
    'increase',
    'indeed',
    'indicate',
    'individual',
    'industry',
    'information',
    'inside',
    'instead',
    'institution',
    'interest',
    'interesting',
    'international',
    'interview',
    'kitchen',
    'letter',
    'magazine',
    'main',
    'maintain',
    'major',
    'majority',
    'manage',
    'management',
    'manager',
    'maybe',
    'medical',
    'memory',
    'mention',
    'message',
    'method',
    'middle',
    'might',
    'military',
    'million',
    'mind',
    'minute',
    'miss',
    'mission',
    'model',
    'modern',
    'moment',
    'money',
    'month',
    'more',
    'morning',
    'most',
    'mother',
    'mouth',
    'move',
    'movement',
    'nearly',
    'necessary',
    'need',
    'network',
    'never',
    'nothing',
    'notice',
    'office',
    'officer',
    'official',
    'often',
    'opportunity',
    'option',
    'owner',
    'page',
    'perform',
    'performance',
    'perhaps',
    'period',
    'position',
    'positive',
    'possible',
    'protect',
    'prove',
    'provide',
    'rather',
    'reach',
    'read',
    'ready',
    'real',
    'reality',
    'realize',
    'really',
    'reason',
    'receive',
    'recent',
    'recently',
    'recognize',
    'record',
    'require',
    'seven',
    'several',
    'somebody',
    'someone',
    'something',
    'sometimes',
    'strategy',
    'street',
    'strong',
    'structure',
    'student',
    'study',
    'stuff',
    'style',
    'subject',
    'success',
    'successful',
    'such',
    'suddenly',
    'suffer',
    'technology',
    'television',
    'themselves',
    'then',
    'theory',
    'those',
    'though',
    'thought',
    'thousand',
    'threat',
    'trade',
    'traditional',
    'training',
    'travel',
    'treat',
    'treatment',
    'usually',
    'value',
    'various',
    'violence',
    'weapon',
    'wear',
    'week',
    'weight',
    'within',
    'without',
    'woman',
    'world',
    'worry',
    'would',
    'write',
    'writer',
    'yourself']
    a=random.choice(lst2)
    return a

def hangman():
    answer=call()
    answerlist=['']
    mylst=[]
    lst=['_' for i in answer]
    if len(answer)>18:
        life=14
    elif len(answer)>15:
        life=13
    elif len(answer)>10:
        life=12
    elif len(answer)>6:
        life=11
    else:
        life=10
    count=0
    print(lst)
    while True :  
        a = input('알파벳을 입력하세요')
        if not a.isalpha():
            print('알파벳이 아닙니다. 다시 입력해주세요\n')
            continue
        elif a in mylst:
            print('이미 입력한 문자입니다. 다시입력하세요\n')
            continue
        elif len(a)>1:
            print('한글자가 아닙니다. 다시 입력하세요\n')
            continue
        
        else:
            mylst.append(a)
        lst=status(answer, mylst,lst[:])
        
        if a in lst:
            print(f'정답에 가까워 지셨습니다.\n{lst}\n')
        else:
            life-=1
            print(f'입력하신 알파벳은 정답안에 존재하지 않습니다.\nLife : {life}\n{lst}\n')
        if isanswer(answer,lst):
            print('정답입니다!')
            break
        if life<1:
            print(f'Game Over\n정답은 {answer}입니다.')
            break
        mylst.sort()
        print(f'현재까지 입력된 문자 : {set(mylst)}')  

hangman()