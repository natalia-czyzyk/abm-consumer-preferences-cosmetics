turtles-own [
  status      ;; defines the power to influence/susceptibility to be influenced
  ITB        ;; intent to buy, once it reaches 1, turtle buys and can influence others
  is-red     ;; determines whether a given agent does not take part in the simulation
  num-meets  ;; the number of times this turtle has met another turtle
]

globals [
  product-value ;; defines the initial ITB for all (with the margin error of +/- 0.1)
  attr-value    ;; defines attribute value
  campaign-count ;; tracking the numbers of campaigns
  campaign-ticks ;; the ticks when campaign happened
  no-ticks      ;; number of ticks
  status-grey  ;; number of turtles who have not bought
  status-green  ;; number of turtles who have bought
  status-red    ;; number of turtles who are not interested
  %-green       ;; percentage of green turtles out of all turtles
]

to setup
  clear-all
  reset-ticks
  setup-product
  setup-turtles
  set-globals
  reset-ticks
end

to setup-product
  assign-values-attr
  let total price + quality + attr-value
  set product-value (total / 300) * 0.9
end

to assign-values-attr
  set attr-value 0
  ifelse attribute-1 = "cruelty-free" [
    set attr-value (attr-value + (33 + 1 / 3))
  ] [
    ifelse attribute-1 = "natural" [
      set attr-value (attr-value + (33 + 1 / 3))
    ] [
      ifelse attribute-1 = "recycled packaging" [
        set attr-value (attr-value + 22)
      ][
        ifelse attribute-1 = "organic" [
          set attr-value (attr-value + 22)
        ][
          ifelse attribute-1 = "fair-trade" [
            set attr-value (attr-value + 22)
          ][
            ifelse attribute-1 = "vegan" [
              set attr-value (attr-value + 11)
            ][
              ifelse attribute-1 = "ecological" [
                set attr-value (attr-value + 11)
              ][
                ifelse attribute-1 = "zero-waste" [
                  set attr-value (attr-value + 11)
                ][
                  ifelse attribute-1 = "bio" [
                    set attr-value (attr-value + 11)
                  ][
                    ifelse attribute-1 = "carbon-neutral" [
                      set attr-value (attr-value + 11)
                    ][
                      error "There is an error in this model"
                    ]
                  ]
                ]
              ]
            ]
          ]
        ]
      ]
    ]
  ]
  ifelse attribute-2 = "cruelty-free" [
    set attr-value (attr-value + (33 + 1 / 3))
  ] [
    ifelse attribute-2 = "natural" [
      set attr-value (attr-value + (33 + 1 / 3))
    ] [
      ifelse attribute-2 = "recycled packaging" [
        set attr-value (attr-value + 22)
      ][
        ifelse attribute-2 = "organic" [
          set attr-value (attr-value + 22)
        ][
          ifelse attribute-2 = "fair-trade" [
            set attr-value (attr-value + 22)
          ][
            ifelse attribute-2 = "vegan" [
              set attr-value (attr-value + 11)
            ][
              ifelse attribute-2 = "ecological" [
                set attr-value (attr-value + 11)
              ][
                ifelse attribute-2 = "zero-waste" [
                  set attr-value (attr-value + 11)
                ][
                  ifelse attribute-2 = "bio" [
                    set attr-value (attr-value + 11)
                  ][
                    ifelse attribute-2 = "carbon-neutral" [
                      set attr-value (attr-value + 11)
                    ][
                      error "There is an error in this model"
                    ]
                  ]
                ]
              ]
            ]
          ]
        ]
      ]
    ]
  ]
  ifelse attribute-3 = "cruelty-free" [
    set attr-value (attr-value + (33 + 1 / 3))
  ] [
    ifelse attribute-3 = "natural" [
      set attr-value (attr-value + (33 + 1 / 3))
    ] [
      ifelse attribute-3 = "recycled packaging" [
        set attr-value (attr-value + 22)
      ][
        ifelse attribute-3 = "organic" [
          set attr-value (attr-value + 22)
        ][
          ifelse attribute-3 = "fair-trade" [
            set attr-value (attr-value + 22)
          ][
            ifelse attribute-3 = "vegan" [
              set attr-value (attr-value + 11)
            ][
              ifelse attribute-3 = "ecological" [
                set attr-value (attr-value + 11)
              ][
                ifelse attribute-3 = "zero-waste" [
                  set attr-value (attr-value + 11)
                ][
                  ifelse attribute-3 = "bio" [
                    set attr-value (attr-value + 11)
                  ][
                    ifelse attribute-3 = "carbon-neutral" [
                      set attr-value (attr-value + 11)
                    ][
                      error "There is an error in this model"
                    ]
                  ]
                ]
              ]
            ]
          ]
        ]
      ]
    ]
  ]
end

to setup-turtles
  create-turtles num-agents [
    setxy random-xcor random-ycor
    set ITB 0
    set num-meets 0
    ifelse (random-float 100 < 10) [  ;; setting up 10% of red agents not participating
      set is-red true
      set color red
    ] [
      set is-red false
      set color gray
    ]

    let rand_val random-float 100
    ifelse (rand_val < 0.4) [
      set status -4
    ]
    [
      ifelse (rand_val < 2 + 0.4) [
        set status -3
      ]
      [
        ifelse (rand_val < 4.8 + 2 + 0.4) [
          set status -2
        ]
        [
          ifelse (rand_val < 10.3 + 4.8 + 2 + 0.4) [
            set status -1
          ]
          [
            ifelse (rand_val < 15.1 + 10.3 + 4.8 + 2 + 0.4) [
              set status 0
            ]
            [
              ifelse (rand_val < 30.2 + 15.1 + 10.3 + 4.8 + 2 + 0.4) [
                set status 1
              ]
              [
                ifelse (rand_val < 21.8 + 30.2 + 15.1 + 10.3 + 4.8 + 2 + 0.4) [
                  set status 2
                ]
                [
                  ifelse (rand_val < 13.5 + 21.8 + 30.2 + 15.1 + 10.3 + 4.8 + 2 + 0.4) [
                    set status 3
                  ]
                  [
                    set status 4
                  ]
                ]
              ]
            ]
          ]
        ]
      ]
    ]
  ]

  ask n-of (count (turtles with [is-red = false]) * %-of-influencers / 100) (turtles with [is-red = false]) [
    set ITB 1
  ]
  update-color

  ask turtles with [ITB = 0] [
    set ITB max (list (ITB + (random-float 0.2 - 0.1 + product-value)) 0 )
]
end

to execute-campaign
  let num-targets round (campaign-reach / 100 * count turtles)
  let targets n-of num-targets turtles
  ask targets [
    if ITB < 1 [
      set ITB ITB + 0.25
    ]
  ]
  set campaign-count campaign-count + 1
end

to go
  ask turtles [
    move
    if ITB >= 1 [ recommend ]
  ]
  update-color
  if ticks > 0 and ticks mod campaign-freq = 0 [
    execute-campaign
  ]

  if ticks = max-ticks [
    stop
  ]
  set-globals
  tick
end

to move
  rt random 100
  lt random 100
  fd 0.05
end

to recommend
  ask other turtles-here with [is-red = false and status < [status] of myself]
    [ if ITB < 1 [
        let difference abs(status - [status] of myself)
        set ITB min (list (ITB + (0.005 * difference)) 1)]
    ]
end

to update-color
  ask turtles [
    if ITB = 1 [
      set color green
    ]
  ]
end

to set-globals
  set no-ticks no-ticks + 1
  set status-red count turtles with [is-red = true]
  set status-grey count turtles with [ITB < 1 and is-red = false]
  set status-green count turtles with [ITB >= 1]
  set %-green round (status-green / (num-agents) * 100)
end
@#$#@#$#@
GRAPHICS-WINDOW
474
26
911
464
-1
-1
13.0
1
10
1
1
1
0
1
1
1
-16
16
-16
16
0
0
1
ticks
30.0

SLIDER
9
433
181
466
price
price
0
100
50.0
1
1
NIL
HORIZONTAL

SLIDER
11
534
183
567
quality
quality
0
100
50.0
1
1
NIL
HORIZONTAL

SLIDER
244
534
416
567
campaign-reach
campaign-reach
1
10
10.0
1
1
NIL
HORIZONTAL

SLIDER
12
204
184
237
num-agents
num-agents
10
1000
500.0
10
1
NIL
HORIZONTAL

SLIDER
12
292
184
325
%-of-influencers
%-of-influencers
1
5
3.0
1
1
NIL
HORIZONTAL

BUTTON
475
518
538
551
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
660
519
723
552
NIL
go\n
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

SLIDER
245
428
417
461
campaign-freq
campaign-freq
500
5000
2500.0
500
1
NIL
HORIZONTAL

INPUTBOX
14
70
169
130
max-ticks
5000.0
1
0
Number

CHOOSER
245
89
393
134
attribute-1
attribute-1
"bio" "cruelty-free" "carbon-neutral" "ecological" "fair-trade" "natural" "recycled packaging" "organic" "vegan" "zero-waste"
4

CHOOSER
246
157
394
202
attribute-2
attribute-2
"bio" "cruelty-free" "carbon-neutral" "ecological" "fair-trade" "natural" "recycled packaging" "organic" "vegan" "zero-waste"
6

CHOOSER
246
227
394
272
attribute-3
attribute-3
"bio" "cruelty-free" "carbon-neutral" "ecological" "fair-trade" "natural" "recycled packaging" "organic" "vegan" "zero-waste"
8

MONITOR
965
257
1034
302
NIL
%-green
2
1
11

PLOT
955
81
1349
231
NIL
ticks
no of agents
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"bought" 1.0 0 -14439633 true "" "plot count turtles with [ITB = 1]"
"didn't buy yet" 1.0 0 -7500403 true "" "plot count turtles with [ITB < 1]"

MONITOR
966
320
1059
365
NIL
product-value
2
1
11

MONITOR
1074
320
1141
365
NIL
attr-value
2
1
11

MONITOR
1052
256
1109
301
%-grey
status-grey / num-agents * 100
2
1
11

MONITOR
1129
256
1186
301
%-red
status-red / num-agents * 100
2
1
11

MONITOR
965
381
1070
426
NIL
campaign-count
2
1
11

TEXTBOX
16
146
166
198
Step 2: define the agents\n\nStep 2.1: select the number of agents
10
0.0
1

TEXTBOX
15
252
165
278
Step 2.2: select the percentage of initial influencers
10
0.0
1

TEXTBOX
15
10
165
62
Step 1: define the number of ticks in the model (recommended duration is 5000)
10
0.0
1

TEXTBOX
14
354
164
419
Step 3: define the product value\n\nStep 3.1: define the relative price (0 - very expensive, 100 - very cheap)
10
0.0
1

TEXTBOX
13
481
163
520
Step 3.2: define the relative quality (0 - poorest quality, 100 - highest quality)
10
0.0
1

TEXTBOX
247
10
397
75
Step 3.3: select up to three attributes the product posseses. If there are less than three, put in the most important attribute more than once.
10
0.0
1

TEXTBOX
245
307
395
411
Step 4: define the marketing campaigns\n\nStep 4.1: select the frequency of campaigns in ticks (the campaign will happen every X ticks, so the higher the number, the lower the frequency)
10
0.0
1

TEXTBOX
244
481
394
520
Step 4.2: select the percentage of randomly chosen agents affected by each campaign
10
0.0
1

TEXTBOX
474
490
624
508
Step 5: setup the simulation
10
0.0
1

TEXTBOX
660
490
810
508
Step 6: run the simulation
10
0.0
1

@#$#@#$#@
## WHAT IS IT?

The aim of the model is to simulate the introduction of a novel sustainable cosmetic to the market and analyse consumers' preferences and behaviours surrounding it. It can be used by companies to measure and test how different product attributes, characteristics and marketing campaigns can influence its spread in the system.

## HOW IT WORKS

A product with a certain product-value is being spread in a system of agents. All agents have different status (marking how persuasive or susceptible they are) and a different ITB (marking their intent to buy the product). They can move freely on the lattice and interact with each other. Each interaction of an influencer with a regular agent can increase the ITB value of the regular agent by a factor of the difference in the respective statuses of the pair. At chosen moments, a marketing campaign occurs, targeting random agents and also increasing their ITB. Once an agent reaches an ITB of 1, they purchase the product, become green and can influence others. The simulation ends after a set number of ticks.

## HOW TO USE IT

First, the user can determine the duration of the simulation, typically recommended at 5000 ticks for optimal results.

Then, a number of agents chosen by the user is created and a certain percentage of them are marked as influencers. These agents are green and have their ITB = 1, meaning they can convince other agents to purchase the product.

Next, 10% of all agents are marked red and they do not participate in the simulation. This number is derived from a survey, reflecting the percentage of people who don't purchase sustainable cosmetics.

The rest of the agents are marked gray and given a status from -4 to 4, indicating their ability to influence others. This distribution is based on survey data. Then, these agents' ITB is set to 0.

Afterward, the user specifies the product parameters:
- the price of the product (0 - very expensive, 100 - very cheap),
- the quality of the product, including ingredients and certifications (0 - very poor, 100 - very good),
- up to three attributes the product posseses, each assigned a value based on consumer importance from the survey.
These three values collectively form the product-value variable, ranging from 0 to 0.9

Each agent is then assigned this product-value variable as their "ITB" characteristic, with a random error margin of +/- 0.1.

Lastly, the user sets marketing campaign parameters, determining the percentage of agents affected by a campaign (increasing their ITB value by 0.25) and the frequency of campaigns (occurring every X ticks, where a higher number means less frequent campaigns).

Once all parameters are configured, the user clicks the "Setup" button to save them and then the "Go" button to start the simulation.

## THINGS TO NOTICE

Observe the changing numbers of gray and green agents on the graph in the interface. The percentages of gray, green and red agents can also be observed on the monitors below. Additionally, you can check the product value and the summarised value of chosen attributes. Lastly, a monitor counting the number of campaigns is also visible.

## THINGS TO TRY

Try running a simulation with different number of agents and starting percentage of influencers.

Set product parameters to the maximum values (observe the product-value and attr-value monitors), run the simulation a couple of times and write down the percentage of green agents. Then repeat it, but with minimum or medium product values and observe the changes.

Try out different settings of the campaign frequency and reach and see how it affects the simulation.

## RELATED MODELS

Virus, Rumour

## CREDITS AND REFERENCES

Natalia Czyżyk, Faculty of Engineering, Wrocław University of Science and Technology, Poland, 2024
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.3.0
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
<experiments>
  <experiment name="1 num turtles" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <steppedValueSet variable="num-agents" first="250" step="250" last="1000"/>
    <enumeratedValueSet variable="%-of-influencers">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="price">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="quality">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="attr-value">
      <value value="55"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-freq">
      <value value="3000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-reach">
      <value value="5"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="2" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="num-agents">
      <value value="500"/>
    </enumeratedValueSet>
    <steppedValueSet variable="%-of-influencers" first="1" step="1" last="5"/>
    <enumeratedValueSet variable="price">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="quality">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="attr-value">
      <value value="55"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-freq">
      <value value="3000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-reach">
      <value value="5"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="3" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="num-agents">
      <value value="500"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="%-of-influencers">
      <value value="3"/>
    </enumeratedValueSet>
    <steppedValueSet variable="price" first="20" step="20" last="100"/>
    <enumeratedValueSet variable="quality">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="attr-value">
      <value value="55"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-freq">
      <value value="3000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-reach">
      <value value="5"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="4" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="num-agents">
      <value value="500"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="%-of-influencers">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="price">
      <value value="50"/>
    </enumeratedValueSet>
    <steppedValueSet variable="quality" first="20" step="20" last="100"/>
    <enumeratedValueSet variable="attr-value">
      <value value="55"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-freq">
      <value value="3000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-reach">
      <value value="5"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="5" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="num-agents">
      <value value="500"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="%-of-influencers">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="price">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="quality">
      <value value="50"/>
    </enumeratedValueSet>
    <steppedValueSet variable="attr-value" first="33" step="11" last="99"/>
    <enumeratedValueSet variable="campaign-freq">
      <value value="3000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-reach">
      <value value="5"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="6" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="num-agents">
      <value value="500"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="%-of-influencers">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="price">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="quality">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="attr-value">
      <value value="55"/>
    </enumeratedValueSet>
    <steppedValueSet variable="campaign-freq" first="1000" step="1000" last="5000"/>
    <enumeratedValueSet variable="campaign-reach">
      <value value="5"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="7" repetitions="100" runMetricsEveryStep="false">
    <setup>setup</setup>
    <go>go</go>
    <metric>%-green</metric>
    <metric>(status-grey / num-agents * 100)</metric>
    <metric>(status-red / num-agents * 100)</metric>
    <enumeratedValueSet variable="max-ticks">
      <value value="5000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="num-agents">
      <value value="500"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="%-of-influencers">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="price">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="quality">
      <value value="50"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="attr-value">
      <value value="55"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="campaign-freq">
      <value value="2500"/>
    </enumeratedValueSet>
    <steppedValueSet variable="campaign-reach" first="2" step="2" last="10"/>
  </experiment>
</experiments>
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
0
@#$#@#$#@
