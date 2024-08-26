from fasthtml.common import *
from tasks_data import data, status_dd, rows_per_page_dd, priority_dd
from fh_frankenui.components import *
from fasthtml.svg import *
import calendar
hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css"),)

app = FastHTML(hdrs=hdrs,debug=True,default_hdrs=False)



avatar_opts =Ul(cls='uk-dropdown-nav uk-nav')(
                            Li(cls='px-2 py-1.5 text-sm')(
                                Div(cls='flex flex-col space-y-1')(
                                    P('sveltecult', cls='text-sm font-medium leading-none'),
                                    P('leader@sveltecult.com', cls='text-xs leading-none text-muted-foreground'))),
                            Li(cls='uk-nav-divider'),
                            Li(A(href='#demo', uk_toggle='', cls='uk-drop-close justify-between')('Profile',Span('⇧⌘P', cls='ml-auto text-xs tracking-widest opacity-60'))),
                            Li(A(href='#demo', uk_toggle='', cls='uk-drop-close justify-between')('Billing',Span('⌘B', cls='ml-auto text-xs tracking-widest opacity-60'))),
                            Li(A(href='#demo', uk_toggle='', cls='uk-drop-close justify-between')('Settings',Span('⌘S', cls='ml-auto text-xs tracking-widest opacity-60'))),
                            Li(A('New Team', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')),
                            Li(cls='uk-nav-divider'),
                            Li(A('Logout', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')))

def MakeTaskForm():
    return Card(Form(
             Div(cls='grid grid-cols-3 gap-2')(
               UkSelect(*[Option(o) for o in ('Documentation','Bug','Feature')],label='Task Type',id='task_type'),
               UkSelect(*[Option(o) for o in ('In Progress','Backlog','Todo','Cancelled','Done')],label='Status',id='task_status'),
               UkSelect(*[Option(o) for o in ('Low','Medium','High')],label='Priority',id='task_priority')),
             UkTextArea(label='Title',placeholder='Please describe the task that needs to be completed'),
             Div(cls='grid grid-cols-2')(
                UkButton(type='button', cls=UkButtonT.ghost, onclick = "document.getElementById('TaskForm').style.display='none'")('Cancel'),
                UkButton(type='button', cls=UkButtonT.primary, onclick = "document.getElementById('TaskForm').style.display='none'")('Submit')),
             header=(H3('Create Task'),P(cls=f'{TextT.muted_sm}')('Fill out the information below to create a new task'))))

check_svg = Svg(xmlns='http://www.w3.org/2000/svg', width='16', height='16', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round', cls='lucide lucide-check mr-2')(Path(d='M20 6 9 17l-5-5'))

@app.get('/')
def homepage():
    return Div(id='TaskForm', style="display:none;")(MakeTaskForm()),Div(cls='p-8')(
            Div(cls='flex items-center justify-between space-y-2')(
                Div(cls='flex-1')(
                    H2('Welcome back!', cls='text-2xl font-bold tracking-tight'),
                    P("Here's a list of your tasks for this month!", 'text-muted-foreground')),
                Div(cls='flex-none')(
                    A(href='#', cls='inline-flex h-8 w-8 items-center justify-center rounded-full bg-accent ring-ring focus:outline-none focus-visible:ring-1')(
                        Span(cls='relative flex h-8 w-8 shrink-0 overflow-hidden rounded-full')(Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed=sveltecult', cls='aspect-square h-full w-full'))),
                    Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(avatar_opts))),
        Div(cls='mt-8 flex items-center justify-between')(
                 Div(cls='flex flex-1 gap-4')(
                     # Table Controls
                     UkInput(cls='w-[250px]',placeholder='Filter task'),
                     UkDropdownButton(
                         label = (Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mr-2 h-4 w-4')(Path(d='M7.49991 0.876892C3.84222 0.876892 0.877075 3.84204 0.877075 7.49972C0.877075 11.1574 3.84222 14.1226 7.49991 14.1226C11.1576 14.1226 14.1227 11.1574 14.1227 7.49972C14.1227 3.84204 11.1576 0.876892 7.49991 0.876892ZM1.82707 7.49972C1.82707 4.36671 4.36689 1.82689 7.49991 1.82689C10.6329 1.82689 13.1727 4.36671 13.1727 7.49972C13.1727 10.6327 10.6329 13.1726 7.49991 13.1726C4.36689 13.1726 1.82707 10.6327 1.82707 7.49972ZM7.50003 4C7.77617 4 8.00003 4.22386 8.00003 4.5V7H10.5C10.7762 7 11 7.22386 11 7.5C11 7.77614 10.7762 8 10.5 8H8.00003V10.5C8.00003 10.7761 7.77617 11 7.50003 11C7.22389 11 7.00003 10.7761 7.00003 10.5V8H4.50003C4.22389 8 4.00003 7.77614 4.00003 7.5C4.00003 7.22386 4.22389 7 4.50003 7H7.00003V4.5C7.00003 4.22386 7.22389 4 7.50003 4Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')),"Status",),
                         options = [f"{a['status']} : {a['count']}" for a in status_dd],
                         btn_cls='text-xs font-medium'),
                     UkDropdownButton(
                         label = (Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mr-2 h-4 w-4')(Path(d='M7.49991 0.876892C3.84222 0.876892 0.877075 3.84204 0.877075 7.49972C0.877075 11.1574 3.84222 14.1226 7.49991 14.1226C11.1576 14.1226 14.1227 11.1574 14.1227 7.49972C14.1227 3.84204 11.1576 0.876892 7.49991 0.876892ZM1.82707 7.49972C1.82707 4.36671 4.36689 1.82689 7.49991 1.82689C10.6329 1.82689 13.1727 4.36671 13.1727 7.49972C13.1727 10.6327 10.6329 13.1726 7.49991 13.1726C4.36689 13.1726 1.82707 10.6327 1.82707 7.49972ZM7.50003 4C7.77617 4 8.00003 4.22386 8.00003 4.5V7H10.5C10.7762 7 11 7.22386 11 7.5C11 7.77614 10.7762 8 10.5 8H8.00003V10.5C8.00003 10.7761 7.77617 11 7.50003 11C7.22389 11 7.00003 10.7761 7.00003 10.5V8H4.50003C4.22389 8 4.00003 7.77614 4.00003 7.5C4.00003 7.22386 4.22389 7 4.50003 7H7.00003V4.5C7.00003 4.22386 7.22389 4 7.50003 4Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')),"Priority",),
                         options = [f"{a['priority']} : {a['count']}" for a in priority_dd],
                         btn_cls='text-xs font-medium'),
                    UkDropdownButton(
                        label=(Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mr-2 h-4 w-4')(Path(d='M5.5 3C4.67157 3 4 3.67157 4 4.5C4 5.32843 4.67157 6 5.5 6C6.32843 6 7 5.32843 7 4.5C7 3.67157 6.32843 3 5.5 3ZM3 5C3.01671 5 3.03323 4.99918 3.04952 4.99758C3.28022 6.1399 4.28967 7 5.5 7C6.71033 7 7.71978 6.1399 7.95048 4.99758C7.96677 4.99918 7.98329 5 8 5H13.5C13.7761 5 14 4.77614 14 4.5C14 4.22386 13.7761 4 13.5 4H8C7.98329 4 7.96677 4.00082 7.95048 4.00242C7.71978 2.86009 6.71033 2 5.5 2C4.28967 2 3.28022 2.86009 3.04952 4.00242C3.03323 4.00082 3.01671 4 3 4H1.5C1.22386 4 1 4.22386 1 4.5C1 4.77614 1.22386 5 1.5 5H3ZM11.9505 10.9976C11.7198 12.1399 10.7103 13 9.5 13C8.28967 13 7.28022 12.1399 7.04952 10.9976C7.03323 10.9992 7.01671 11 7 11H1.5C1.22386 11 1 10.7761 1 10.5C1 10.2239 1.22386 10 1.5 10H7C7.01671 10 7.03323 10.0008 7.04952 10.0024C7.28022 8.8601 8.28967 8 9.5 8C10.7103 8 11.7198 8.8601 11.9505 10.0024C11.9668 10.0008 11.9833 10 12 10H13.5C13.7761 10 14 10.2239 14 10.5C14 10.7761 13.7761 11 13.5 11H12C11.9833 11 11.9668 10.9992 11.9505 10.9976ZM8 10.5C8 9.67157 8.67157 9 9.5 9C10.3284 9 11 9.67157 11 10.5C11 11.3284 10.3284 12 9.5 12C8.67157 12 8 11.3284 8 10.5Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')),'View'),
                        options = [Div(cls='flex flex-column')((check_svg, o)) for o in ['Title','Status','Priority']]),
                    UkButton('Create Task',cls='uk-button-primary text-xs font-medium', onclick = "document.getElementById('TaskForm').style.display='block'"))),
             Div(cls='uk-overflow-auto mt-4 rounded-md border border-border')(
                 Table(cls='uk-table uk-table-middle uk-table-divider uk-table-hover uk-table-small')(
                     # Table header
                     Thead(Tr(Th(cls='uk-table-shrink p-2')(Input(type='checkbox', onclick='return false', cls='uk-checkbox')),
                             *[Th(cls='p-2')(o) for o in ['Task','Title','Status','Priority']],
                             Th(cls='uk-table-shrink p-2'))),
                     # Table Body (Tasks content)
                     Tbody(
                         *[Tr(**{'=':'true'}, **{'?':''}, **{'"uk-active"':''}, **{':':''}, **{'""}':''}, cls=a['selected'])(
                             Td(cls='uk-table-shrink p-2')(CheckboxX(cls='uk-checkbox')),
                             Td(a['id'], cls='p-2'),
                             Td(cls='uk-table-expand max-w-[500px] truncate p-2')(Span(a['label'], cls='uk-label capitalize'),Span(a['title'], cls='font-medium')),
                             Td(cls='uk-text-nowrap p-2')(Span(a['status'])),
                             Td(cls='uk-text-nowrap p-2')(Span(a['priority'])),
                             Td(cls='p-2')(
                                 Button(cls='uk-icon-button uk-icon-button-xsmall')(Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M3.625 7.5C3.625 8.12132 3.12132 8.625 2.5 8.625C1.87868 8.625 1.375 8.12132 1.375 7.5C1.375 6.87868 1.87868 6.375 2.5 6.375C3.12132 6.375 3.625 6.87868 3.625 7.5ZM8.625 7.5C8.625 8.12132 8.12132 8.625 7.5 8.625C6.87868 8.625 6.375 8.12132 6.375 7.5C6.375 6.87868 6.87868 6.375 7.5 6.375C8.12132 6.375 8.625 6.87868 8.625 7.5ZM12.5 8.625C13.1213 8.625 13.625 8.12132 13.625 7.5C13.625 6.87868 13.1213 6.375 12.5 6.375C11.8787 6.375 11.375 6.87868 11.375 7.5C11.375 8.12132 11.8787 8.625 12.5 8.625Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                                 Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(
                                     Ul(cls='uk-dropdown-nav uk-nav')(
                                         Li(A('Edit', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')),
                                         Li(A('Make a copy', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')),
                                         Li(A('Favorite', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')),
                                         Li(cls='uk-nav-divider'),
                                         Li(A(href='#demo', uk_toggle='', cls='uk-drop-close justify-between')('Delete',Span('⌘⌫', cls='ml-auto text-xs tracking-widest opacity-60')))))))
                          for a in data])),
             # Table Footer
             Div(cls='mt-4 flex items-center justify-between px-2')(
                 Div('1 of 100 row(s) selected.', cls='flex-1 text-sm text-muted-foreground'),
                 Div(cls='flex flex-none items-center space-x-8')(
                     Div(cls='flex items-center space-x-2')(
                       P('Rows per page', cls='text-sm font-medium'),
                       UkSelect(*Options((10,20,30,40,50)))),
                     Div('Page 1 of 10', cls='flex w-[100px] items-center justify-center text-sm font-medium'),
                     Div(cls='flex items-center space-x-2')(
                         Button(disabled='', cls='uk-icon-button uk-icon-button-small hidden lg:inline-flex')(Span('Go to last page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M6.85355 3.85355C7.04882 3.65829 7.04882 3.34171 6.85355 3.14645C6.65829 2.95118 6.34171 2.95118 6.14645 3.14645L2.14645 7.14645C1.95118 7.34171 1.95118 7.65829 2.14645 7.85355L6.14645 11.8536C6.34171 12.0488 6.65829 12.0488 6.85355 11.8536C7.04882 11.6583 7.04882 11.3417 6.85355 11.1464L3.20711 7.5L6.85355 3.85355ZM12.8536 3.85355C13.0488 3.65829 13.0488 3.34171 12.8536 3.14645C12.6583 2.95118 12.3417 2.95118 12.1464 3.14645L8.14645 7.14645C7.95118 7.34171 7.95118 7.65829 8.14645 7.85355L12.1464 11.8536C12.3417 12.0488 12.6583 12.0488 12.8536 11.8536C13.0488 11.6583 13.0488 11.3417 12.8536 11.1464L9.20711 7.5L12.8536 3.85355Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                         Button(disabled='', cls='uk-icon-button uk-icon-button-small')(Span('Go to previous page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M8.84182 3.13514C9.04327 3.32401 9.05348 3.64042 8.86462 3.84188L5.43521 7.49991L8.86462 11.1579C9.05348 11.3594 9.04327 11.6758 8.84182 11.8647C8.64036 12.0535 8.32394 12.0433 8.13508 11.8419L4.38508 7.84188C4.20477 7.64955 4.20477 7.35027 4.38508 7.15794L8.13508 3.15794C8.32394 2.95648 8.64036 2.94628 8.84182 3.13514Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                         Button(uk_toggle='#demo', cls='uk-icon-button uk-icon-button-small')(
                             Span('Go to next page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M6.1584 3.13508C6.35985 2.94621 6.67627 2.95642 6.86514 3.15788L10.6151 7.15788C10.7954 7.3502 10.7954 7.64949 10.6151 7.84182L6.86514 11.8418C6.67627 12.0433 6.35985 12.0535 6.1584 11.8646C5.95694 11.6757 5.94673 11.3593 6.1356 11.1579L9.565 7.49985L6.1356 3.84182C5.94673 3.64036 5.95694 3.32394 6.1584 3.13508Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                         Button(uk_toggle='#demo', cls='uk-icon-button uk-icon-button-small hidden lg:inline-flex')(
                             Span('Go to last page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M2.14645 11.1464C1.95118 11.3417 1.95118 11.6583 2.14645 11.8536C2.34171 12.0488 2.65829 12.0488 2.85355 11.8536L6.85355 7.85355C7.04882 7.65829 7.04882 7.34171 6.85355 7.14645L2.85355 3.14645C2.65829 2.95118 2.34171 2.95118 2.14645 3.14645C1.95118 3.34171 1.95118 3.65829 2.14645 3.85355L5.79289 7.5L2.14645 11.1464ZM8.14645 11.1464C7.95118 11.3417 7.95118 11.6583 8.14645 11.8536C8.34171 12.0488 8.65829 12.0488 8.85355 11.8536L12.8536 7.85355C13.0488 7.65829 13.0488 7.34171 12.8536 7.14645L8.85355 3.14645C8.65829 2.95118 8.34171 2.95118 8.14645 3.14645C7.95118 3.34171 7.95118 3.65829 8.14645 3.85355L11.7929 7.5L8.14645 11.1464Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))))))))
serve()
