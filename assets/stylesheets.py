def GetStyle(name="default") -> str:
        return eval(f"__{name}")


__uniC = {
        "pbackground": "",
        "pcolor": "#B2B2B2"
}
__uniColors = F"""
* {{ 
        background-color: transparent;
        color: {__uniC['pcolor']}; 
}}

#MainWindow, #centralwidget {{
        background-color: transparent;
}}

#TopBar {{ 
        background-color: #050505;
        border-top-left-radius:10px;
}}

#TopBarOpen {{ 
        background-color: #050505;
        border-top-left-radius:0px;
}}

#LeftModal {{ 
        background-color: #111111;
        border-top-left-radius: 10px; 
        border-bottom-left-radius: 15px; 
}}

#LeftModalMax {{ 
        background-color: #111111; 
        border-top-left-radius: 0px; 
        border-bottom-left-radius: 0px;
}}

#RightModal {{
        background-color: #111111;
        border-top: 1px solid #050505;
}}

#ContentPanel {{
        background-color: #101010;
        border-top: 1px solid #050505;
        border-left: 1px solid #050505;
}}
#ContentPages {{
        border-right: 1px solid #050505;
        border-top: 1px solid #050505;
}}

#ContentTitles {{
        background-color: #090909;
}}


#ToggleLeftBtn {{
        background-color: #050505;
        border: none;
        border-top-left-radius: 10px;
        border-bottom-left-radius: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
}}

#ToggleLeftBtn:hover {{
        background-color: #91111111;
        border: none;
}}

#ToggleLeftBtnOpen {{
        background-color: #111111;
        border: none;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
        border-top-right-radius: 10px;
        border-bottom-right-radius: 0px;
}}

#ToggleLeftBtnOpen:hover {{
        background-color: #91111111;
        border: none;
}}

#ToggleRightBtn {{
        background-color: #090909;
        border: none;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
}}

#ToggleRightBtn:hover  {{
        background-color: #91111111;
        border: none;
}}

#ToggleRightBtnOpen {{
        background-color: #111111;
        border:none;
        border-top-left-radius: 10px;
        border-bottom-left-radius: 0px;
         border-top-right-radius: 0px;
         border-bottom-right-radius: 0px;
}}

#ToggleRightBtnOpen:hover {{
        background-color: #91111111; border: none;
}}

#MinimizeBtn, #MaximizeBtn, #CloseBtn {{
        background-color: transparent;
        border: none;
}}

#MinimizeBtn:hover, #MaximizeBtn:hover, #CloseBtn:hover {{
        border-bottom: 1px solid #111111;
}}

#MinimizeBtn:hover, #MaximizeBtn:hover {{
        background-color: #101010;
}}

#CloseBtn:hover {{
        background-color: #916c0e17;
}}

#MoveGrip {{
        background-color: #11696969;
        border-radius: 5px;
}}

#MoveGrip:hover {{
        background-color: #13696969;
}}

#TitleLb {{
        color: #2D2D2D;
}}

#TitleLb:hover {{
        color: #2E2E2E;
}}

#ErroMsg {{
        color: #916c0e17;
}}

#UsernameLb, #PasswordLb, #LoginBtn {{
        border-radius: 5px;
        border: 1px solid #33696969;
        color: #7D7D7D;
}}

#UsernameLb:focus, #PasswordLb:focus, #LoginBtn:focus {{
        color: #ADADAD;
        border-bottom: 1px solid #99696969;
}}

#StayConnectBox {{
        color: #5D5D5D;
}}

#StayConnectBox:checked {{
        color: #7D7D7D;
}}

#StayConnectBox:focus {{
        border-bottom: 1px solid #99696969;
}}

#LoginBtn:hover {{
        background-color: #11696969;
        color: #4D4D4D;
}}
"""




__default = """
* { background-color: transparent; color: #B2B2B2; }

#MainWindow, #centralwidget { background-color: transparent; }

#TopBar { background-color: #050505; border-top-left-radius:10px;}
#TopBarOpen { background-color: #050505; border-top-left-radius:0px; }

#LeftModal { background-color: #111111; border-top-left-radius: 10px; border-bottom-left-radius: 15px; }
#LeftModalMax { background-color: #111111; border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

#RightModal { background-color: #111111; border-top: 1px solid #050505;}

#ContentPanel {background-color: #101010; border-top: 1px solid #050505; border-left: 1px solid #050505; }
#ContentPages {border-right: 1px solid #050505; border-top: 1px solid #050505;}

#ContentTitles { background-color: #090909 ; }

/* Toggle buttons */
#ToggleLeftBtn { background-color: #050505; border: none;
border-top-left-radius: 10px; border-bottom-left-radius: 0px;
border-top-right-radius: 0px; border-bottom-right-radius: 0px;}
#ToggleLeftBtn:hover { background-color: #91111111; border: none; }
#ToggleLeftBtnOpen { background-color: #111111; border: none; 
border-top-left-radius: 0px; border-bottom-left-radius: 0px;
border-top-right-radius: 10px; border-bottom-right-radius: 0px; }
#ToggleLeftBtnOpen:hover { background-color: #91111111; border: none; }
/**/
#ToggleRightBtn { background-color: #090909; border: none;
border-top-left-radius: 0px; border-bottom-left-radius: 0px;
border-top-right-radius: 0px; border-bottom-right-radius: 0px;}
#ToggleRightBtn:hover  { background-color: #91111111; border: none; }
#ToggleRightBtnOpen { background-color: #111111; border:none;
border-top-left-radius: 10px; border-bottom-left-radius: 0px;
 border-top-right-radius: 0px; border-bottom-right-radius: 0px; }
#ToggleRightBtnOpen:hover { background-color: #91111111; border: none; }
/*	*/
/*  windows state buttons */
#MinimizeBtn, #MaximizeBtn, #CloseBtn { background-color: transparent; border: none; }
#MinimizeBtn:hover, #MaximizeBtn:hover, #CloseBtn:hover {	border-bottom: 1px solid #111111;}
#MinimizeBtn:hover, #MaximizeBtn:hover { background-color: #101010; }

#CloseBtn:hover { background-color: #916c0e17; }
/*	*/
#MoveGrip { background-color: #11696969; border-radius: 5px; }
#MoveGrip:hover { background-color: #13696969; }
#TitleLb { color: #2D2D2D;}
#TitleLb:hover {color: #2E2E2E;}

#ErroMsg {Color: #916c0e17; }

#UsernameLb, #PasswordLb, #LoginBtn { border-radius: 5px; border: 1px solid #33696969; color: #7D7D7D;}
#UsernameLb:focus, #PasswordLb:focus, #LoginBtn:focus { color: #ADADAD; border-bottom: 1px solid #99696969; }

#StayConnectBox { color: #5D5D5D }
#StayConnectBox:checked { color: #7D7D7D;  }
#StayConnectBox:focus { border-bottom: 1px solid #99696969; }

#LoginBtn:hover {background-color: #11696969; color: #4D4D4D;}
"""