#############################################################################
# Generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#  Aug 22, 2022 12:20:22 PM +0530  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background #1e1e1e 
    wm focusmodel $top passive
    wm geometry $top 633x430+584+369
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4644 1161
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Keylogger v2 - by @hirushaadi"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu $top.m46 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    
set site_3_0 $top.m46
    $top.m46 add cascade \
        -menu "$top.m46.men50" -activebackground {} -activeforeground {} \
        -background {} -command {{}} -font {} -foreground {} -label Menu 
    menu $site_3_0.men50 \
        -activebackground beige -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men50 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label Save 
    $site_3_0.men50 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label Build 
    
set site_3_0 $top.m46
    $top.m46 add cascade \
        -menu "$top.m46.men48" -activebackground {} -activeforeground {} \
        -background {} -command {{}} -font {} -foreground {} -label Actions 
    menu $site_3_0.men48 \
        -activebackground beige -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men48 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label Build 
    $site_3_0.men48 add separator \
        -background {} 
    $site_3_0.men48 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label Reset 
    
set site_3_0 $top.m46
    $top.m46 add cascade \
        -menu "$top.m46.men47" -activebackground {} -activeforeground {} \
        -background {} -command {{}} -font {} -foreground {} -label Other 
    menu $site_3_0.men47 \
        -activebackground beige -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men47 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label {Source Code} 
    $site_3_0.men47 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label About 
    $site_3_0.men47 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label Help 
    frame $top.fra53 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 125 -width 165 
    vTcl:DefineAlias "$top.fra53" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent54 \
        -background #191919 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground #ffffff -insertbackground black -width 234 
    vTcl:DefineAlias "$top.ent54" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -activeforeground SystemButtonText -anchor w -background #1e1e1e \
        -compound left -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #49b618 -text {Executable Name: } 
    vTcl:DefineAlias "$top.lab55" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra53 \
        -in $top -x 0 -relx 0.032 -y 0 -rely 0.256 -width 0 -relwidth 0.261 \
        -height 0 -relheight 0.291 -anchor nw -bordermode ignore 
    place $top.ent54 \
        -in $top -x 0 -relx 0.032 -y 0 -rely 0.14 -width 234 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.032 -y 0 -rely 0.093 -width 0 -relwidth 0.259 \
        -height 0 -relheight 0.049 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

