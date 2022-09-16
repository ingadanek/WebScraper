from extract_data import extract

def test_extract_should_strip_texts():
    html = '<b> this should be stripped </b>'
    got = extract(html, '//b')
    expected = ['this should be stripped']
    assert got == expected


def test_extract_converts_newlines_to_spaces():
    html = '<b>this should be stripped\nthis is a new line</b>'
    got = extract(html, '//b')
    expected = ['this should be stripped this is a new line']
    assert got == expected

def test_scrapper_reallife_webpage():
    with open('projects/scraper/leroymerlin.html', encoding = 'utf-8') as stream:
        html = stream.read()
    got = extract(html, '//*[@id="maincontent"]/div[4]/div[1]/div[9]/ol/li/div[2]/strong/a')
    expected = [
        'Lean-To Ladder 10 Step Aluminium GRAVITY',
        'Lean-To Ladder 10 Step Fibreglass SUPERLIGHT',
        'Lean-To Ladder 16 Step Aluminium GRAVITY',
        'Ladder 3-IN-1 Tri Function 6 Step Aluminium GRAVITY',
        'Telescopic Ladder 10 Step 3.2m Aluminium',
        'Lean-To Ladder A-frame 12 Step Aluminium GRAVITY',
        'Lean-To Ladder 14 Step Aluminium GRAVITY',
        'Lean-To Ladder 12 Step Fibreglass SUPERLIGHT',
        'Lean-To Ladder A-frame 14 Step Fibreglass SUPERLIGHT',
        'Oak Wood 10" Manual Pepper Grinders Mills Set',
        'Folding camping mat',
        'FOLDING MAGNETIC UPRIGHT EXERCISE BIKE',
        'Step Ladder A-Frame 8 Step Fibreglass',
        'Step ladder A-frame 10 Step Fibreglass GRAVITY',
        'Multi Purpose Ladder Fibreglass, 6 Steps as a A frame, 12 Steps as a Straight Ladder SUPERLIGHT',
        'Ladder Dual Function 6/12 step Aluminium GRAVITY',
        'Ladder 3 in 1 Tri-Function 7 Step Aluminium GRAVITY',
        'Ladder multipurpose WONDER LADDER 6 step A-frame & 12 straight aluminium'
    ]
    assert got == expected

   
