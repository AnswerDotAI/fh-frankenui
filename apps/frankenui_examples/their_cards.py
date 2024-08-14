from fasthtml.common import *
from fasthtml.components import Uk_input_tag, Rect, Uk_select

# import requests
# web_component_url = 'https://raw.githubusercontent.com/franken-ui/examples/master/public/js/franken-wc%400.0.6/wc.iife.js'
# response = requests.get(web_component_url)
# js_content = response.text
# wc = Script(js_content)
# INFO:     127.0.0.1:59334 - "GET /%7B%60https%3A//api.dicebear.com/8.x/lorelei/svg?seed=${a.name}`} HTTP/1.1" 404 Not Found
# INFO:     127.0.0.1:59334 - "GET /%7B%60https%3A//api.dicebear.com/8.x/lorelei/svg?seed=${a.name}`} HTTP/1.1" 404 Not Found

# Should match https://examples.franken-ui.dev/cards
hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),#Script(src="/js/uikit@3.21.6/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),#Script(src="/js/uikit@3.21.6/icons.min.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css"), #Script(type="module", src="/js/franken-wc@0.0.6/wc.iife.js"),
        # Link(rel="preload", href="/fonts/geist-font/fonts/GeistVariableVF.woff2", as_="font", type="font/woff2", crossorigin=""),
        # Link(rel="preload", href="/fonts/geist-font/fonts/GeistMonoVariableVF.woff2", as_="font", type="font/woff2", crossorigin=""),
        # Link(rel="stylesheet", href="/fonts/geist-font/style.css"),
        # Link(rel="stylesheet", href="/_astro/master.CZ5-T1HD.css"),
        # wc
)
app = FastHTML(default_hdrs=False, hdrs=hdrs)


# '---\r\nimport Master from "layouts/master.astro";\r\n---'
# Master(
@app.get('/')
def home():
    return Div(cls='grid gap-6 p-8 lg:grid-cols-2 xl:grid-cols-3')(
        Div(cls='space-y-6')(
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Create an account', cls='text-2xl font-semibold tracking-tight'),
                    P('Enter your email below to create your account', cls='text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body space-y-4 py-0')(
                    Div(cls='grid grid-cols-2 gap-6')(
                        Button(uk_toggle='#demo', cls='uk-button uk-button-default')(
                            Svg(viewbox='0 0 438.549 438.549', cls='mr-2 h-4 w-4')(
                                Path(fill='currentColor', d='M409.132 114.573c-19.608-33.596-46.205-60.194-79.798-79.8-33.598-19.607-70.277-29.408-110.063-29.408-39.781 0-76.472 9.804-110.063 29.408-33.596 19.605-60.192 46.204-79.8 79.8C9.803 148.168 0 184.854 0 224.63c0 47.78 13.94 90.745 41.827 128.906 27.884 38.164 63.906 64.572 108.063 79.227 5.14.954 8.945.283 11.419-1.996 2.475-2.282 3.711-5.14 3.711-8.562 0-.571-.049-5.708-.144-15.417a2549.81 2549.81 0 01-.144-25.406l-6.567 1.136c-4.187.767-9.469 1.092-15.846 1-6.374-.089-12.991-.757-19.842-1.999-6.854-1.231-13.229-4.086-19.13-8.559-5.898-4.473-10.085-10.328-12.56-17.556l-2.855-6.57c-1.903-4.374-4.899-9.233-8.992-14.559-4.093-5.331-8.232-8.945-12.419-10.848l-1.999-1.431c-1.332-.951-2.568-2.098-3.711-3.429-1.142-1.331-1.997-2.663-2.568-3.997-.572-1.335-.098-2.43 1.427-3.289 1.525-.859 4.281-1.276 8.28-1.276l5.708.853c3.807.763 8.516 3.042 14.133 6.851 5.614 3.806 10.229 8.754 13.846 14.842 4.38 7.806 9.657 13.754 15.846 17.847 6.184 4.093 12.419 6.136 18.699 6.136 6.28 0 11.704-.476 16.274-1.423 4.565-.952 8.848-2.383 12.847-4.285 1.713-12.758 6.377-22.559 13.988-29.41-10.848-1.14-20.601-2.857-29.264-5.14-8.658-2.286-17.605-5.996-26.835-11.14-9.235-5.137-16.896-11.516-22.985-19.126-6.09-7.614-11.088-17.61-14.987-29.979-3.901-12.374-5.852-26.648-5.852-42.826 0-23.035 7.52-42.637 22.557-58.817-7.044-17.318-6.379-36.732 1.997-58.24 5.52-1.715 13.706-.428 24.554 3.853 10.85 4.283 18.794 7.952 23.84 10.994 5.046 3.041 9.089 5.618 12.135 7.708 17.705-4.947 35.976-7.421 54.818-7.421s37.117 2.474 54.823 7.421l10.849-6.849c7.419-4.57 16.18-8.758 26.262-12.565 10.088-3.805 17.802-4.853 23.134-3.138 8.562 21.509 9.325 40.922 2.279 58.24 15.036 16.18 22.559 35.787 22.559 58.817 0 16.178-1.958 30.497-5.853 42.966-3.9 12.471-8.941 22.457-15.125 29.979-6.191 7.521-13.901 13.85-23.131 18.986-9.232 5.14-18.182 8.85-26.84 11.136-8.662 2.286-18.415 4.004-29.263 5.146 9.894 8.562 14.842 22.077 14.842 40.539v60.237c0 3.422 1.19 6.279 3.572 8.562 2.379 2.279 6.136 2.95 11.276 1.995 44.163-14.653 80.185-41.062 108.068-79.226 27.88-38.161 41.825-81.126 41.825-128.906-.01-39.771-9.818-76.454-29.414-110.049z')
                            ),
                            'Github'
                        ),
                        Button(uk_toggle='#demo', cls='uk-button uk-button-default')(
                            Svg(role='img', viewbox='0 0 24 24', cls='mr-2 h-4 w-4')(
                                Path(fill='currentColor', d='M12.48 10.92v3.28h7.84c-.24 1.84-.853 3.187-1.787 4.133-1.147 1.147-2.933 2.4-6.053 2.4-4.827 0-8.6-3.893-8.6-8.72s3.773-8.72 8.6-8.72c2.6 0 4.507 1.027 5.907 2.347l2.307-2.307C18.747 1.44 16.133 0 12.48 0 5.867 0 .307 5.387.307 12s5.56 12 12.173 12c3.573 0 6.267-1.173 8.373-3.36 2.16-2.16 2.84-5.213 2.84-7.667 0-.76-.053-1.467-.173-2.053H12.48z')
                            ),
                            'Google'
                        )
                    ),
                    Div(cls='relative')(
                        Div(cls='absolute inset-0 flex items-center')(
                            Span(cls='w-full border-t border-border')
                        ),
                        Div(cls='relative flex justify-center text-xs uppercase')(
                            Span('Or continue with', cls='bg-background px-2 text-muted-foreground')
                        )
                    ),
                    Div(cls='space-y-2')(
                        Label('Email', fr='email', cls='uk-form-label'),
                        Input(id='email', type='text', placeholder='m@example.com', cls='uk-input')
                    ),
                    Div(cls='space-y-2')(
                        Label('Password', fr='password', cls='uk-form-label'),
                        Input(id='password', type='password', placeholder='Password', cls='uk-input')
                    )
                ),
                Div(cls='uk-card-footer')(
                    Button('Create account', uk_toggle='#demo', cls='uk-button uk-button-primary w-full')
                )
            ),
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Payment Method', cls='text-2xl font-semibold tracking-tight'),
                    P('Add a new payment method to your account.', cls='text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body space-y-6 py-0')(
                    Div(cls='grid grid-cols-3 gap-4')(
                        Button(uk_toggle='#demo', cls='uk-button uk-button-default h-20 w-full border-2 border-primary')(
                            Div(cls='flex flex-col items-center justify-center')(
                                Svg(xmlns='http://www.w3.org/2000/svg', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', cls='mb-3 h-6 w-6')(
                                    Rect(width='20', height='14', x='2', y='5', rx='2'),
                                    Path(d='M2 10h20')
                                ),
                                'Card'
                            )
                        ),
                        Button(uk_toggle='#demo', cls='uk-button uk-button-default h-20 w-full')(
                            Div(cls='flex flex-col items-center justify-center')(
                                Svg(role='img', viewbox='0 0 24 24', cls='mb-3 h-6 w-6')(
                                    Path(d='M7.076 21.337H2.47a.641.641 0 0 1-.633-.74L4.944.901C5.026.382 5.474 0 5.998 0h7.46c2.57 0 4.578.543 5.69 1.81 1.01 1.15 1.304 2.42 1.012 4.287-.023.143-.047.288-.077.437-.983 5.05-4.349 6.797-8.647 6.797h-2.19c-.524 0-.968.382-1.05.9l-1.12 7.106zm14.146-14.42a3.35 3.35 0 0 0-.607-.541c-.013.076-.026.175-.041.254-.93 4.778-4.005 7.201-9.138 7.201h-2.19a.563.563 0 0 0-.556.479l-1.187 7.527h-.506l-.24 1.516a.56.56 0 0 0 .554.647h3.882c.46 0 .85-.334.922-.788.06-.26.76-4.852.816-5.09a.932.932 0 0 1 .923-.788h.58c3.76 0 6.705-1.528 7.565-5.946.36-1.847.174-3.388-.777-4.471z', fill='currentColor')
                                ),
                                'Card'
                            )
                        ),
                        Button(uk_toggle='#demo', cls='uk-button uk-button-default h-20 w-full')(
                            Div(cls='flex flex-col items-center justify-center')(
                                Svg(role='img', viewbox='0 0 24 24', cls='mb-3 h-6 w-6')(
                                    Path(d='M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701', fill='currentColor')
                                ),
                                'Apple'
                            )
                        )
                    ),
                    Div(cls='space-y-2')(
                        Label('Name', fr='name', cls='uk-form-label'),
                        Input(id='name', type='text', placeholder='John Doe', cls='uk-input')
                    ),
                    Div(cls='space-y-2')(
                        Label('Card number', fr='card_number', cls='uk-form-label'),
                        Input(id='card_number', type='text', cls='uk-input')
                    ),
                    Div(cls='grid grid-cols-3 gap-4')(
                        Div(cls='space-y-2')(
                            Label('Expires', fr='expire_month', cls='uk-form-label'),
                            Div(cls='h-9')(
                                Uk_select(name='expire_month', uk_cloak='')(
                                    Option('January', selected=''),
                                    Option('February'),
                                    Option('March'),
                                    Option('April'),
                                    Option('May'),
                                    Option('June'),
                                    Option('July'),
                                    Option('August'),
                                    Option('September'),
                                    Option('October'),
                                    Option('November'),
                                    Option('December')
                                )
                            )
                        ),
                        Div(cls='space-y-2')(
                            Label('Year', fr='expire_year', cls='uk-form-label'),
                            Div(cls='h-9')(
                                Uk_select(name='expire_year', uk_cloak='')(
                                    Option('2023', selected=''),
                                    Option('2024'),
                                    Option('2025'),
                                    Option('2026'),
                                    Option('2027'),
                                    Option('2028'),
                                    Option('2029'),
                                    Option('2030')
                                )
                            )
                        ),
                        Div(cls='space-y-2')(
                            Label('CVV', fr='cvv', cls='uk-form-label'),
                            Input(type='text', id='cvv', placeholder='CVV', cls='uk-input')
                        )
                    )
                ),
                Div(cls='uk-card-footer')(
                    Button('Continue', uk_toggle='#demo', cls='uk-button uk-button-primary w-full')
                )
            )
        ),
        Div(cls='space-y-6')(
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Team Members', cls='font-semibold leading-none tracking-tight'),
                    P('Invite your team members to collaborate.', cls='mt-1.5 text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body space-y-6')(
                    '{\r\n            [\r\n              { name: "Sofia Davis", email: "m@example.com", role: "Owner" },\r\n              { name: "Jackson Lee", email: "p@example.com", role: "Member" },\r\n            ].map((a) => (',
                    Div(cls='flex items-center space-x-4')(
                        Span(cls='relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full bg-accent')(
                            Img(src='{`https://api.dicebear.com/8.x/lorelei/svg?seed=${a.name}`}', cls='aspect-square h-full w-full')
                        ),
                        Div(cls='flex-1')(
                            P('{a.name}', cls='text-sm font-medium leading-none'),
                            P('{a.email}', cls='text-sm text-muted-foreground')
                        ),
                        Button(type='button', cls='uk-button uk-button-default')(
                            '{a.role}',
                            Span(uk_drop_parent_icon='', cls='ml-2')
                        ),
                        Div(uk_drop='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop w-[252px]')(
                            Div(cls='m-1 flex items-center px-2 py-1.5')(
                                Span(uk_icon='icon: search; ratio: 0.8', cls='opacity-50'),
                                Input(placeholder='Select a new role', type='text', cls='block w-full bg-transparent pl-2 text-sm focus:outline-none')
                            ),
                            Ul(cls='uk-dropdown-nav')(
                                Li(cls='uk-nav-divider'),
                                Li(
                                    A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                        Div(
                                            Div('Viewer'),
                                            Div('Can view and comment.', cls='text-sm text-muted-foreground')
                                        )
                                    )
                                ),
                                Li(
                                    A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                        Div(
                                            Div('Developer'),
                                            Div('Can view, comment and edit.', cls='text-sm text-muted-foreground')
                                        )
                                    )
                                ),
                                Li(
                                    A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                        Div(
                                            Div('Billing'),
                                            Div('Can view, comment and manage billing.', cls='text-sm text-muted-foreground')
                                        )
                                    )
                                ),
                                Li(
                                    A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                        Div(
                                            Div('Owner'),
                                            Div('Admin-level to all resources.', cls='text-sm text-muted-foreground')
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    '))\r\n          }'
                )
            ),
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Share this document', cls='font-semibold leading-none tracking-tight'),
                    P('Anyone with the link can view this document.', cls='mt-1.5 text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body pt-0')(
                    Div(cls='flex gap-x-2')(
                        Div(cls='flex-1')(
                            Input(readonly='', value='http://example.com/link/to/document', cls='uk-input')
                        ),
                        Div(cls='flex-none')(
                            Button('Copy Link', uk_toggle='#demo', cls='uk-button uk-button-default')
                        )
                    ),
                    Hr(cls='uk-divider-icon my-4'),
                    Div(cls='space-y-4')(
                        H4('People with access', cls='text-sm font-medium'),
                        '{\r\n              [\r\n                {\r\n                  name: "Olivia Martin",\r\n                  email: "m@example.com",\r\n                  role: "Read and write access",\r\n                },\r\n                {\r\n                  name: "Isabella Nguyen",\r\n                  email: "b@example.com",\r\n                  role: "Read-only access",\r\n                },\r\n                {\r\n                  name: "Sofia Davis",\r\n                  email: "p@example.com",\r\n                  role: "Read-only access",\r\n                },\r\n              ].map((a) => (',
                        Div(cls='flex items-center space-x-4')(
                            Span(cls='relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full bg-accent')(
                                Img(src='{`https://api.dicebear.com/8.x/lorelei/svg?seed=${a.name}`}', cls='aspect-square h-full w-full')
                            ),
                            Div(cls='flex-1')(
                                P('{a.name}', cls='text-sm font-medium leading-none'),
                                P('{a.email}', cls='text-sm text-muted-foreground')
                            ),
                            Div(cls='h-9 w-[200px]')(
                                Uk_select(uk_cloak='')(
                                    '{["Read and write access", "Read-only access"].map(\r\n                        (b) => (',
                                    Option('{b}', selected='{b', **{'=':'a.role}'}),
                                    '),\r\n                      )}'
                                )
                            )
                        ),
                        '))\r\n            }'
                    )
                )
            ),
            Div(cls='uk-card uk-card-body space-y-2')(
                Label('Pick a date', cls='uk-form-label'),
                Div(cls='')(
                    Button(cls='uk-button uk-button-default w-[260px]')(
                        Div(uk_toggle='#demo', cls='flex gap-x-2')(
                            Svg(xmlns='http://www.w3.org/2000/svg', width='16', height='16', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round', cls='lucide lucide-calendar-days')(
                                Path(d='M8 2v4'),
                                Path(d='M16 2v4'),
                                Rect(width='18', height='18', x='3', y='4', rx='2'),
                                Path(d='M3 10h18'),
                                Path(d='M8 14h.01'),
                                Path(d='M12 14h.01'),
                                Path(d='M16 14h.01'),
                                Path(d='M8 18h.01'),
                                Path(d='M12 18h.01'),
                                Path(d='M16 18h.01')
                            ),
                            'Jan 20, 2024 - Feb 09, 2024'
                        )
                    )
                )
            ),
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Notifications', cls='font-semibold leading-none tracking-tight'),
                    P('Choose what you want to be notified about.', cls='mt-1.5 text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body pt-0')(
                    Ul(cls='uk-nav uk-nav-secondary')(
                        Li(cls='-mx-1')(
                            A(href='#demo', uk_toggle='', cls='')(
                                Div(cls='flex gap-x-4')(
                                    Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-5 w-5 flex-none')(
                                        Path(d='M8.60124 1.25086C8.60124 1.75459 8.26278 2.17927 7.80087 2.30989C10.1459 2.4647 12 4.41582 12 6.79999V10.25C12 11.0563 12.0329 11.7074 12.7236 12.0528C12.931 12.1565 13.0399 12.3892 12.9866 12.6149C12.9333 12.8406 12.7319 13 12.5 13H8.16144C8.36904 13.1832 8.49997 13.4513 8.49997 13.75C8.49997 14.3023 8.05226 14.75 7.49997 14.75C6.94769 14.75 6.49997 14.3023 6.49997 13.75C6.49997 13.4513 6.63091 13.1832 6.83851 13H2.49999C2.2681 13 2.06664 12.8406 2.01336 12.6149C1.96009 12.3892 2.06897 12.1565 2.27638 12.0528C2.96708 11.7074 2.99999 11.0563 2.99999 10.25V6.79999C2.99999 4.41537 4.85481 2.46396 7.20042 2.3098C6.73867 2.17908 6.40036 1.75448 6.40036 1.25086C6.40036 0.643104 6.89304 0.150421 7.5008 0.150421C8.10855 0.150421 8.60124 0.643104 8.60124 1.25086ZM7.49999 3.29999C5.56699 3.29999 3.99999 4.86699 3.99999 6.79999V10.25L4.00002 10.3009C4.0005 10.7463 4.00121 11.4084 3.69929 12H11.3007C10.9988 11.4084 10.9995 10.7463 11 10.3009L11 10.25V6.79999C11 4.86699 9.43299 3.29999 7.49999 3.29999Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                                    ),
                                    Div(cls='flex-1')(
                                        P('Everything'),
                                        P('Email digest, mentions & all activity.', cls='text-sm text-muted-foreground')
                                    )
                                )
                            )
                        ),
                        Li(cls='uk-active -mx-1')(
                            A(href='#demo', uk_toggle='', cls='')(
                                Div(cls='flex gap-x-4')(
                                    Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mt-px h-5 w-5')(
                                        Path(d='M7.5 0.875C5.49797 0.875 3.875 2.49797 3.875 4.5C3.875 6.15288 4.98124 7.54738 6.49373 7.98351C5.2997 8.12901 4.27557 8.55134 3.50407 9.31167C2.52216 10.2794 2.02502 11.72 2.02502 13.5999C2.02502 13.8623 2.23769 14.0749 2.50002 14.0749C2.76236 14.0749 2.97502 13.8623 2.97502 13.5999C2.97502 11.8799 3.42786 10.7206 4.17091 9.9883C4.91536 9.25463 6.02674 8.87499 7.49995 8.87499C8.97317 8.87499 10.0846 9.25463 10.8291 9.98831C11.5721 10.7206 12.025 11.8799 12.025 13.5999C12.025 13.8623 12.2376 14.0749 12.5 14.0749C12.7623 14.075 12.975 13.8623 12.975 13.6C12.975 11.72 12.4778 10.2794 11.4959 9.31166C10.7244 8.55135 9.70025 8.12903 8.50625 7.98352C10.0187 7.5474 11.125 6.15289 11.125 4.5C11.125 2.49797 9.50203 0.875 7.5 0.875ZM4.825 4.5C4.825 3.02264 6.02264 1.825 7.5 1.825C8.97736 1.825 10.175 3.02264 10.175 4.5C10.175 5.97736 8.97736 7.175 7.5 7.175C6.02264 7.175 4.825 5.97736 4.825 4.5Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                                    ),
                                    Div(cls='flex-1')(
                                        P('Available'),
                                        P('Only mentions and comments.', cls='text-sm text-muted-foreground')
                                    )
                                )
                            )
                        ),
                        Li(cls='-mx-1')(
                            A(href='#demo', uk_toggle='', cls='')(
                                Div(cls='flex gap-x-4')(
                                    Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mt-px h-5 w-5')(
                                        Path(d='M13.3536 2.35355C13.5488 2.15829 13.5488 1.84171 13.3536 1.64645C13.1583 1.45118 12.8417 1.45118 12.6464 1.64645L10.6828 3.61012C9.70652 3.21671 8.63759 3 7.5 3C4.30786 3 1.65639 4.70638 0.0760002 7.23501C-0.0253338 7.39715 -0.0253334 7.60288 0.0760014 7.76501C0.902945 9.08812 2.02314 10.1861 3.36061 10.9323L1.64645 12.6464C1.45118 12.8417 1.45118 13.1583 1.64645 13.3536C1.84171 13.5488 2.15829 13.5488 2.35355 13.3536L4.31723 11.3899C5.29348 11.7833 6.36241 12 7.5 12C10.6921 12 13.3436 10.2936 14.924 7.76501C15.0253 7.60288 15.0253 7.39715 14.924 7.23501C14.0971 5.9119 12.9769 4.81391 11.6394 4.06771L13.3536 2.35355ZM9.90428 4.38861C9.15332 4.1361 8.34759 4 7.5 4C4.80285 4 2.52952 5.37816 1.09622 7.50001C1.87284 8.6497 2.89609 9.58106 4.09974 10.1931L9.90428 4.38861ZM5.09572 10.6114L10.9003 4.80685C12.1039 5.41894 13.1272 6.35031 13.9038 7.50001C12.4705 9.62183 10.1971 11 7.5 11C6.65241 11 5.84668 10.8639 5.09572 10.6114Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                                    ),
                                    Div(cls='flex-1')(
                                        P('Ignoring'),
                                        P('Turn off all notifications.', cls='text-sm text-muted-foreground')
                                    )
                                )
                            )
                        )
                    )
                )
            )
        ),
        Div(cls='space-y-6')(
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Report an issue', cls='font-semibold leading-none tracking-tight'),
                    P('What area are you having problems with?', cls='mt-1.5 text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body space-y-6 py-0')(
                    Div(cls='grid grid-cols-2 gap-2')(
                        Div(cls='space-y-2')(
                            Label('Area', cls='uk-form-label'),
                            Div(cls='h-9')(
                                Uk_select(uk_cloak='')(
                                    '{\r\n                    ["Team", "Billing", "Account", "Deployment", "Support"].map(\r\n                      (a) =>',
                                    Option('{a}', selected='{a', **{'=':'Billing'}, **{'}':''}),
                                    ',\r\n                    )\r\n                  }'
                                )
                            )
                        ),
                        Div(cls='space-y-2')(
                            Label('Severity', cls='uk-form-label'),
                            Div(cls='h-9')(
                                Uk_select(uk_cloak='')(
                                    '{\r\n                    [\r\n                      "Severity 1 (Highest)",\r\n                      "Severity 2",\r\n                      "Severity 3",\r\n                      "Severity 4 (Lowest)",\r\n                    ].map((a) => (',
                                    Option('{a}', selected='{a', **{'=':'Severity 2'}, **{'}':''}),
                                    '))\r\n                  }'
                                )
                            )
                        )
                    ),
                    Div(cls='space-y-2')(
                        Label('Subject', fr='subject', cls='uk-form-label'),
                        Input(id='subject', placeholder='I need help with', type='text', cls='uk-input')
                    ),
                    Div(cls='space-y-2')(
                        Label('Description', fr='description', cls='uk-form-label'),
                        Textarea(id='description', placeholder='Please include all information relevant to your issue', cls='uk-textarea')
                    ),
                    Div(cls='space-y-2')(
                        Label('Tags', cls='uk-form-label'),
                        Div(cls='min-h-9')(
                            Uk_input_tag(state='danger', value='Spam,Invalid')
                        )
                    )
                ),
                Div(cls='uk-card-footer flex justify-between')(
                    Button('Cancel', uk_toggle='#demo', cls='uk-button uk-button-ghost'),
                    Button('Submit', uk_toggle='#demo', cls='uk-button uk-button-primary')
                )
            ),
            Div(cls='uk-card uk-card-body space-y-6')(
                Div(cls='flex gap-x-4')(
                    Div(cls='flex-1')(
                        H3('franken/ui', cls='font-semibold leading-none tracking-tight'),
                        P('HTML-first, framework-agnostic, beautifully designed components\r\n              that you can truly copy and paste into your site. Accessible.\r\n              Customizable. Open Source.', cls='text-sm text-muted-foreground')
                    ),
                    Div(cls='flex-none')(
                        Div(cls='flex items-center space-x-1 rounded-md bg-secondary text-secondary-foreground')(
                            A(href='https://github.com/sveltecult/franken-ui', target='_blank', cls='inline-flex h-9 items-center justify-center whitespace-nowrap rounded-md bg-secondary px-3 py-2 text-sm font-medium text-secondary-foreground shadow-none transition-colors hover:bg-secondary/80 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50')(
                                Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mr-2 h-4 w-4')(
                                    Path(d='M6.97942 1.25171L6.9585 1.30199L5.58662 4.60039C5.54342 4.70426 5.44573 4.77523 5.3336 4.78422L1.7727 5.0697L1.71841 5.07405L1.38687 5.10063L1.08608 5.12475C0.820085 5.14607 0.712228 5.47802 0.914889 5.65162L1.14406 5.84793L1.39666 6.06431L1.43802 6.09974L4.15105 8.42374C4.23648 8.49692 4.2738 8.61176 4.24769 8.72118L3.41882 12.196L3.40618 12.249L3.32901 12.5725L3.25899 12.866C3.19708 13.1256 3.47945 13.3308 3.70718 13.1917L3.9647 13.0344L4.24854 12.861L4.29502 12.8326L7.34365 10.9705C7.43965 10.9119 7.5604 10.9119 7.6564 10.9705L10.705 12.8326L10.7515 12.861L11.0354 13.0344L11.2929 13.1917C11.5206 13.3308 11.803 13.1256 11.7411 12.866L11.671 12.5725L11.5939 12.249L11.5812 12.196L10.7524 8.72118C10.7263 8.61176 10.7636 8.49692 10.849 8.42374L13.562 6.09974L13.6034 6.06431L13.856 5.84793L14.0852 5.65162C14.2878 5.47802 14.18 5.14607 13.914 5.12475L13.6132 5.10063L13.2816 5.07405L13.2274 5.0697L9.66645 4.78422C9.55432 4.77523 9.45663 4.70426 9.41343 4.60039L8.04155 1.30199L8.02064 1.25171L7.89291 0.944609L7.77702 0.665992C7.67454 0.419604 7.32551 0.419604 7.22303 0.665992L7.10715 0.944609L6.97942 1.25171ZM7.50003 2.60397L6.50994 4.98442C6.32273 5.43453 5.89944 5.74207 5.41351 5.78103L2.84361 5.98705L4.8016 7.66428C5.17183 7.98142 5.33351 8.47903 5.2204 8.95321L4.62221 11.461L6.8224 10.1171C7.23842 9.86302 7.76164 9.86302 8.17766 10.1171L10.3778 11.461L9.77965 8.95321C9.66654 8.47903 9.82822 7.98142 10.1984 7.66428L12.1564 5.98705L9.58654 5.78103C9.10061 5.74207 8.67732 5.43453 8.49011 4.98442L7.50003 2.60397Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                                ),
                                'Star'
                            ),
                            Div(data_orientation='vertical', role='none', cls='h-[20px] w-[1px] shrink-0 bg-border'),
                            Button(type='button', cls='inline-flex h-9 items-center justify-center whitespace-nowrap rounded-md bg-secondary px-2 py-2 text-sm font-medium text-secondary-foreground shadow-none transition-colors hover:bg-secondary/80 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50')(
                                Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='h-4 w-4 text-secondary-foreground')(
                                    Path(d='M3.13523 6.15803C3.3241 5.95657 3.64052 5.94637 3.84197 6.13523L7.5 9.56464L11.158 6.13523C11.3595 5.94637 11.6759 5.95657 11.8648 6.15803C12.0536 6.35949 12.0434 6.67591 11.842 6.86477L7.84197 10.6148C7.64964 10.7951 7.35036 10.7951 7.15803 10.6148L3.15803 6.86477C2.95657 6.67591 2.94637 6.35949 3.13523 6.15803Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                                )
                            ),
                            Div(uk_drop='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(
                                Ul(cls='uk-dropdown-nav')(
                                    Li('Suggested Lists', cls='uk-nav-header'),
                                    Li(cls='uk-nav-divider'),
                                    Li(
                                        A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                            Svg(xmlns='http://www.w3.org/2000/svg', width='16', height='16', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round', cls='lucide lucide-check mr-2')(
                                                Path(d='M20 6 9 17l-5-5')
                                            ),
                                            'Future ideas'
                                        )
                                    ),
                                    Li(
                                        A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                            Span('My stack', cls='ml-6')
                                        )
                                    ),
                                    Li(
                                        A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                            Span('Inspiration', cls='ml-6')
                                        )
                                    ),
                                    Li(
                                        A(href='#demo', uk_toggle='', cls='uk-drop-close')(
                                            Svg(xmlns='http://www.w3.org/2000/svg', width='16', height='16', viewbox='0 0 24 24', fill='none', stroke='currentColor', stroke_width='2', stroke_linecap='round', stroke_linejoin='round', cls='lucide lucide-plus mr-2')(
                                                Path(d='M5 12h14'),
                                                Path(d='M12 5v14')
                                            ),
                                            'Create List'
                                        )
                                    )
                                )
                            )
                        )
                    )
                ),
                Div(cls='flex space-x-4 text-sm text-muted-foreground')(
                    Div(cls='flex items-center')(
                        Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mr-1 h-3 w-3 fill-sky-400 text-sky-400')(
                            Path(d='M0.877075 7.49991C0.877075 3.84222 3.84222 0.877075 7.49991 0.877075C11.1576 0.877075 14.1227 3.84222 14.1227 7.49991C14.1227 11.1576 11.1576 14.1227 7.49991 14.1227C3.84222 14.1227 0.877075 11.1576 0.877075 7.49991ZM7.49991 1.82708C4.36689 1.82708 1.82708 4.36689 1.82708 7.49991C1.82708 10.6329 4.36689 13.1727 7.49991 13.1727C10.6329 13.1727 13.1727 10.6329 13.1727 7.49991C13.1727 4.36689 10.6329 1.82708 7.49991 1.82708Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                        ),
                        'TypeScript'
                    ),
                    Div(cls='flex items-center')(
                        Svg(width='15', height='15', viewbox='0 0 15 15', fill='none', xmlns='http://www.w3.org/2000/svg', cls='mr-1 h-3 w-3')(
                            Path(d='M6.97942 1.25171L6.9585 1.30199L5.58662 4.60039C5.54342 4.70426 5.44573 4.77523 5.3336 4.78422L1.7727 5.0697L1.71841 5.07405L1.38687 5.10063L1.08608 5.12475C0.820085 5.14607 0.712228 5.47802 0.914889 5.65162L1.14406 5.84793L1.39666 6.06431L1.43802 6.09974L4.15105 8.42374C4.23648 8.49692 4.2738 8.61176 4.24769 8.72118L3.41882 12.196L3.40618 12.249L3.32901 12.5725L3.25899 12.866C3.19708 13.1256 3.47945 13.3308 3.70718 13.1917L3.9647 13.0344L4.24854 12.861L4.29502 12.8326L7.34365 10.9705C7.43965 10.9119 7.5604 10.9119 7.6564 10.9705L10.705 12.8326L10.7515 12.861L11.0354 13.0344L11.2929 13.1917C11.5206 13.3308 11.803 13.1256 11.7411 12.866L11.671 12.5725L11.5939 12.249L11.5812 12.196L10.7524 8.72118C10.7263 8.61176 10.7636 8.49692 10.849 8.42374L13.562 6.09974L13.6034 6.06431L13.856 5.84793L14.0852 5.65162C14.2878 5.47802 14.18 5.14607 13.914 5.12475L13.6132 5.10063L13.2816 5.07405L13.2274 5.0697L9.66645 4.78422C9.55432 4.77523 9.45663 4.70426 9.41343 4.60039L8.04155 1.30199L8.02064 1.25171L7.89291 0.944609L7.77702 0.665992C7.67454 0.419604 7.32551 0.419604 7.22303 0.665992L7.10715 0.944609L6.97942 1.25171ZM7.50003 2.60397L6.50994 4.98442C6.32273 5.43453 5.89944 5.74207 5.41351 5.78103L2.84361 5.98705L4.8016 7.66428C5.17183 7.98142 5.33351 8.47903 5.2204 8.95321L4.62221 11.461L6.8224 10.1171C7.23842 9.86302 7.76164 9.86302 8.17766 10.1171L10.3778 11.461L9.77965 8.95321C9.66654 8.47903 9.82822 7.98142 10.1984 7.66428L12.1564 5.98705L9.58654 5.78103C9.10061 5.74207 8.67732 5.43453 8.49011 4.98442L7.50003 2.60397Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd')
                        ),
                        '20k'
                    ),
                    Div('Updated April 2023')
                )
            ),
            Div(cls='uk-card')(
                Div(cls='uk-card-header')(
                    H3('Cookie Settings', cls='font-semibold leading-none tracking-tight'),
                    P('Manage your cookie settings here.', cls='mt-1.5 text-sm text-muted-foreground')
                ),
                Div(cls='uk-card-body space-y-6 py-0')(
                    '{\r\n            [\r\n              {\r\n                id: "strict",\r\n                title: "Strictly Necessary",\r\n                description:\r\n                  "These cookies are essential in order to use the website and use its features.",\r\n              },\r\n              {\r\n                id: "functional",\r\n                title: "Functional Cookies",\r\n                description:\r\n                  "These cookies allow the website to provide personalized functionality.",\r\n              },\r\n              {\r\n                id: "performant",\r\n                title: "Performance Cookies",\r\n                description:\r\n                  "These cookies help to improve the performance of the website.",\r\n              },\r\n            ].map((a) => (',
                    Div(cls='flex items-center justify-between gap-2')(
                        Label(fr='{a.id}', cls='flex flex-1 flex-col space-y-1 text-sm font-medium leading-none')(
                            Span('{a.title}'),
                            Span('{a.description}', cls='font-normal leading-snug text-muted-foreground')
                        ),
                        Input(checked='{a.id', **{'=':'strict'}, **{'}':''}, id='{a.id}', type='checkbox', cls='uk-toggle-switch uk-toggle-switch-primary flex-none')
                    ),
                    '))\r\n          }'
                ),
                Div(cls='uk-card-footer')(
                    Button('Save preferences', uk_toggle='#demo', cls='uk-button uk-button-default w-full')
                )
            )
        )
    )
