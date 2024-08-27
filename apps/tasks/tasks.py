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

hotkeys = (('Profile','⇧⌘P'),('Billing','⌘B'),('Settings','⌘S'),('New Team',''),('Logout',''))
avatar_opts =Ul(cls='uk-dropdown-nav uk-nav')(
                            Li(cls='px-2 py-1.5 text-sm')(
                                Div(cls='flex flex-col space-y-1')(
                                    P('sveltecult', cls='text-sm font-medium leading-none'),
                                    P('leader@sveltecult.com', cls='text-xs leading-none text-muted-foreground'))),
                            Li(cls='uk-nav-divider'),
                            *map(lambda x: Li(A(cls='uk-drop-close justify-between')(x[0],Span(x[1],cls='ml-auto text-xs tracking-widest opacity-60'))), hotkeys))

def MakeTaskForm():
    return Form(cls='uk-modal-body uk-modal-dialog space-y-6')(
             UkH3('Create Task'),P(cls=TextT.muted_sm)('Fill out the information below to create a new task',),
             Div(cls='grid grid-cols-3 gap-2')(
               UkSelect(*map(Option,('Documentation','Bug','Feature')),                  label='Task Type',id='task_type'),
               UkSelect(*map(Option,('In Progress','Backlog','Todo','Cancelled','Done')),label='Status',   id='task_status'),
               UkSelect(*map(Option,('Low','Medium','High')),                            label='Priority', id='task_priority')),
             UkTextArea(label='Title',placeholder='Please describe the task that needs to be completed'),
             Div(cls='grid grid-cols-2')(
                UkButton(cls=UkButtonT.ghost   + ' uk-modal-close')('Cancel'),
                UkButton(cls=UkButtonT.primary + ' uk-modal-close')('Submit')))

check_svg = Svg(xmlns='http://www.w3.org/2000/svg', width='16', height='16', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round', cls='lucide lucide-check mr-2')(Path(d='M20 6 9 17l-5-5'))

def UkIconButton(*c, cls='uk-icon-button-sm'):
    return Button(cls='uk-icon-button ' + stringify(cls))(*c)
@app.get('/')
def homepage():
    modal = Div(id='TaskForm',cls='uk-modal p-6 uk-modal-container', uk_modal=True)(MakeTaskForm())

    page_heading =Div(cls='flex items-center justify-between space-y-2')(
                Div(cls='space-y-2')(
                    UkH2('Welcome back!'),P("Here's a list of your tasks for this month!", cls=TextT.muted_sm)),
                Div(A(href='#', cls='h-8 w-8 inline-flex rounded-full bg-accent ring-ring')(Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed=sveltecult')),
                    Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(avatar_opts)))

    table_controls =(UkInput(cls='w-[250px]',placeholder='Filter task'),
                     UkDropdownButton(
                         label = "Status",
                         options = [f"{a['status']} : {a['count']}" for a in status_dd],
                         btn_cls=(TextT.medium_xs, 'uk-button-default')),
                     UkDropdownButton(
                         label = "Priority",
                         options = [f"{a['priority']} : {a['count']}" for a in priority_dd],
                         btn_cls=(TextT.medium_xs,'uk-button-default')),
                    UkDropdownButton(
                        label='View',
                        options = [Div(cls='flex flex-column')((check_svg, o)) for o in ['Title','Status','Priority']],
                        btn_cls=(TextT.medium_xs,'uk-button-default')),
                    UkButton('Create Task',cls=('uk-button-primary', TextT.medium_xs), uk_toggle="target: #TaskForm"))
    return modal,Div(cls='p-8')(
            page_heading,
        Div(cls='mt-8 flex items-center justify-between')(
                 Div(cls='flex flex-1 gap-4')(table_controls)),
             Div(cls='uk-overflow-auto mt-4 rounded-md border border-border')(
                 Table(cls='uk-table uk-table-middle uk-table-divider uk-table-hover uk-table-small')(
                     # Table header
                     Thead(Tr(Th(cls='uk-table-shrink p-2')(Input(type='checkbox', cls='uk-checkbox')),
                             *[Th(cls='p-2')(o) for o in ['Task','Title','Status','Priority']],
                             Th(cls='uk-table-shrink p-2'))),
                     # Table Body (Tasks content)
                     Tbody(
                         *[Tr(cls=a['selected'])(
                             Td(cls='uk-table-shrink p-2')(CheckboxX(cls='uk-checkbox')),
                             Td(a['id'], cls='p-2'),
                             Td(cls='uk-table-expand max-w-[500px] truncate p-2')(Span(a['label'], cls='uk-label capitalize'),Span(a['title'], cls='font-medium')),
                             *map(lambda x: Td(cls='uk-text-nowrap p-2 uk-text-capitalize')(x), (a['status'],a['priority'])) ,
                             Td(cls='p-2')(
                                 Button(cls='uk-icon-button uk-icon-button-xsmall')(Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M3.625 7.5C3.625 8.12132 3.12132 8.625 2.5 8.625C1.87868 8.625 1.375 8.12132 1.375 7.5C1.375 6.87868 1.87868 6.375 2.5 6.375C3.12132 6.375 3.625 6.87868 3.625 7.5ZM8.625 7.5C8.625 8.12132 8.12132 8.625 7.5 8.625C6.87868 8.625 6.375 8.12132 6.375 7.5C6.375 6.87868 6.87868 6.375 7.5 6.375C8.12132 6.375 8.625 6.87868 8.625 7.5ZM12.5 8.625C13.1213 8.625 13.625 8.12132 13.625 7.5C13.625 6.87868 13.1213 6.375 12.5 6.375C11.8787 6.375 11.375 6.87868 11.375 7.5C11.375 8.12132 11.8787 8.625 12.5 8.625Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                                 Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(
                                     Ul(cls='uk-dropdown-nav uk-nav')(
                                         *map(lambda x: Li(A(x, cls='uk-drop-close justify-between')), ('Edit','Make a copy','Favorite', ('Delete',Span('⌘⌫', cls='ml-auto text-xs tracking-widest opacity-60'))))))))
                           for a in data[:10]])),
             # Table Footer
             Div(cls='mt-4 flex items-center justify-between px-2')(
                 Div('1 of 100 row(s) selected.', cls='flex-1 text-sm text-muted-foreground'),
                 Div(cls='flex flex-none items-center space-x-8')(
                     Div('Page 1 of 10', cls='flex w-[100px] items-center justify-center text-sm font-medium'),
                     Div(cls='flex items-center space-x-2')(
                         Button(cls='uk-icon-button uk-icon-button-small hidden lg:inline-flex')(Span('Go to last page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M6.85355 3.85355C7.04882 3.65829 7.04882 3.34171 6.85355 3.14645C6.65829 2.95118 6.34171 2.95118 6.14645 3.14645L2.14645 7.14645C1.95118 7.34171 1.95118 7.65829 2.14645 7.85355L6.14645 11.8536C6.34171 12.0488 6.65829 12.0488 6.85355 11.8536C7.04882 11.6583 7.04882 11.3417 6.85355 11.1464L3.20711 7.5L6.85355 3.85355ZM12.8536 3.85355C13.0488 3.65829 13.0488 3.34171 12.8536 3.14645C12.6583 2.95118 12.3417 2.95118 12.1464 3.14645L8.14645 7.14645C7.95118 7.34171 7.95118 7.65829 8.14645 7.85355L12.1464 11.8536C12.3417 12.0488 12.6583 12.0488 12.8536 11.8536C13.0488 11.6583 13.0488 11.3417 12.8536 11.1464L9.20711 7.5L12.8536 3.85355Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                         UkIconButton(Span('Go to previous page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M8.84182 3.13514C9.04327 3.32401 9.05348 3.64042 8.86462 3.84188L5.43521 7.49991L8.86462 11.1579C9.05348 11.3594 9.04327 11.6758 8.84182 11.8647C8.64036 12.0535 8.32394 12.0433 8.13508 11.8419L4.38508 7.84188C4.20477 7.64955 4.20477 7.35027 4.38508 7.15794L8.13508 3.15794C8.32394 2.95648 8.64036 2.94628 8.84182 3.13514Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                         UkIconButton(Span('Go to next page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M6.1584 3.13508C6.35985 2.94621 6.67627 2.95642 6.86514 3.15788L10.6151 7.15788C10.7954 7.3502 10.7954 7.64949 10.6151 7.84182L6.86514 11.8418C6.67627 12.0433 6.35985 12.0535 6.1584 11.8646C5.95694 11.6757 5.94673 11.3593 6.1356 11.1579L9.565 7.49985L6.1356 3.84182C5.94673 3.64036 5.95694 3.32394 6.1584 3.13508Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))),
                         Button(cls='uk-icon-button uk-icon-button-small hidden lg:inline-flex')(
                             Span('Go to last page', cls='sr-only'),
                             Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4')(Path(d='M2.14645 11.1464C1.95118 11.3417 1.95118 11.6583 2.14645 11.8536C2.34171 12.0488 2.65829 12.0488 2.85355 11.8536L6.85355 7.85355C7.04882 7.65829 7.04882 7.34171 6.85355 7.14645L2.85355 3.14645C2.65829 2.95118 2.34171 2.95118 2.14645 3.14645C1.95118 3.34171 1.95118 3.65829 2.14645 3.85355L5.79289 7.5L2.14645 11.1464ZM8.14645 11.1464C7.95118 11.3417 7.95118 11.6583 8.14645 11.8536C8.34171 12.0488 8.65829 12.0488 8.85355 11.8536L12.8536 7.85355C13.0488 7.65829 13.0488 7.34171 12.8536 7.14645L8.85355 3.14645C8.65829 2.95118 8.34171 2.95118 8.14645 3.14645C7.95118 3.34171 7.95118 3.65829 8.14645 3.85355L11.7929 7.5L8.14645 11.1464Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'))))))))
serve()
