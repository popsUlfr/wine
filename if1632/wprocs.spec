name	wprocs
type	win16

14 pascal FileOpenDlgProc(word word word long) FileOpenDlgProc
15 pascal FileSaveDlgProc(word word word long) FileSaveDlgProc
16 pascal ColorDlgProc(word word word long) ColorDlgProc
17 pascal FindTextDlgProc(word word word long) FindTextDlgProc16
18 pascal ReplaceTextDlgProc(word word word long) ReplaceTextDlgProc16
19 pascal PrintSetupDlgProc(word word word long) PrintSetupDlgProc
20 pascal PrintDlgProc(word word word long) PrintDlgProc
24 pascal16 TASK_Reschedule() TASK_Reschedule
27 pascal EntryAddrProc(word word) NE_GetEntryPoint
28 pascal MyAlloc(word word word) NE_AllocateSegment
29 pascal DefResourceHandler(word word word) NE_DefResourceHandler
30 pascal FormatCharDlgProc(word word word long) FormatCharDlgProc16
 
# Interrupt vectors 0-255 are ordinals 100-355
# The 'word' parameter are the flags pushed on the stack by the interrupt
100 register INT_Int00Handler(word) BUILTIN_DefaultIntHandler
101 register INT_Int01Handler(word) BUILTIN_DefaultIntHandler
102 register INT_Int02Handler(word) BUILTIN_DefaultIntHandler
103 register INT_Int03Handler(word) BUILTIN_DefaultIntHandler
104 register INT_Int04Handler(word) BUILTIN_DefaultIntHandler
105 register INT_Int05Handler(word) BUILTIN_DefaultIntHandler
106 register INT_Int06Handler(word) BUILTIN_DefaultIntHandler
107 register INT_Int07Handler(word) BUILTIN_DefaultIntHandler
108 register INT_Int08Handler(word) BUILTIN_DefaultIntHandler
109 register INT_Int09Handler(word) BUILTIN_DefaultIntHandler
110 register INT_Int0aHandler(word) BUILTIN_DefaultIntHandler
111 register INT_Int0bHandler(word) BUILTIN_DefaultIntHandler
112 register INT_Int0cHandler(word) BUILTIN_DefaultIntHandler
113 register INT_Int0dHandler(word) BUILTIN_DefaultIntHandler
114 register INT_Int0eHandler(word) BUILTIN_DefaultIntHandler
115 register INT_Int0fHandler(word) BUILTIN_DefaultIntHandler
116 register INT_Int10Handler(word) INT_Int10Handler
117 register INT_Int11Handler(word) INT_Int11Handler
118 register INT_Int12Handler(word) INT_Int12Handler
119 register INT_Int13Handler(word) INT_Int13Handler
120 register INT_Int14Handler(word) BUILTIN_DefaultIntHandler
121 register INT_Int15Handler(word) INT_Int15Handler
122 register INT_Int16Handler(word) BUILTIN_DefaultIntHandler
123 register INT_Int17Handler(word) BUILTIN_DefaultIntHandler
124 register INT_Int18Handler(word) BUILTIN_DefaultIntHandler
125 register INT_Int19Handler(word) BUILTIN_DefaultIntHandler
126 register INT_Int1aHandler(word) INT_Int1aHandler
127 register INT_Int1bHandler(word) BUILTIN_DefaultIntHandler
128 register INT_Int1cHandler(word) BUILTIN_DefaultIntHandler
129 register INT_Int1dHandler(word) BUILTIN_DefaultIntHandler
130 register INT_Int1eHandler(word) BUILTIN_DefaultIntHandler
131 register INT_Int1fHandler(word) BUILTIN_DefaultIntHandler
132 register INT_Int20Handler(word) INT_Int20Handler
133 register INT_Int21Handler(word) DOS3Call
134 register INT_Int22Handler(word) BUILTIN_DefaultIntHandler
135 register INT_Int23Handler(word) BUILTIN_DefaultIntHandler
136 register INT_Int24Handler(word) BUILTIN_DefaultIntHandler
# Note: int 25 and 26 don't pop the flags from the stack
137 register INT_Int25Handler()     INT_Int25Handler
138 register INT_Int26Handler()     INT_Int26Handler
139 register INT_Int27Handler(word) BUILTIN_DefaultIntHandler
140 register INT_Int28Handler(word) BUILTIN_DefaultIntHandler
141 register INT_Int29Handler(word) BUILTIN_DefaultIntHandler
142 register INT_Int2aHandler(word) INT_Int2aHandler
143 register INT_Int2bHandler(word) BUILTIN_DefaultIntHandler
144 register INT_Int2cHandler(word) BUILTIN_DefaultIntHandler
145 register INT_Int2dHandler(word) BUILTIN_DefaultIntHandler
146 register INT_Int2eHandler(word) BUILTIN_DefaultIntHandler
147 register INT_Int2fHandler(word) INT_Int2fHandler
148 register INT_Int30Handler(word) BUILTIN_DefaultIntHandler
149 register INT_Int31Handler(word) INT_Int31Handler
150 register INT_Int32Handler(word) BUILTIN_DefaultIntHandler
151 register INT_Int33Handler(word) BUILTIN_DefaultIntHandler
152 register INT_Int34Handler(word) BUILTIN_DefaultIntHandler
153 register INT_Int35Handler(word) BUILTIN_DefaultIntHandler
154 register INT_Int36Handler(word) BUILTIN_DefaultIntHandler
155 register INT_Int37Handler(word) BUILTIN_DefaultIntHandler
156 register INT_Int38Handler(word) BUILTIN_DefaultIntHandler
157 register INT_Int39Handler(word) BUILTIN_DefaultIntHandler
158 register INT_Int3aHandler(word) BUILTIN_DefaultIntHandler
159 register INT_Int3bHandler(word) BUILTIN_DefaultIntHandler
160 register INT_Int3cHandler(word) BUILTIN_DefaultIntHandler
161 register INT_Int3dHandler(word) INT_Int3dHandler
162 register INT_Int3eHandler(word) BUILTIN_DefaultIntHandler
163 register INT_Int3fHandler(word) BUILTIN_DefaultIntHandler
164 register INT_Int40Handler(word) BUILTIN_DefaultIntHandler
165 register INT_Int41Handler(word) BUILTIN_DefaultIntHandler
166 register INT_Int42Handler(word) BUILTIN_DefaultIntHandler
167 register INT_Int43Handler(word) BUILTIN_DefaultIntHandler
168 register INT_Int44Handler(word) BUILTIN_DefaultIntHandler
169 register INT_Int45Handler(word) BUILTIN_DefaultIntHandler
170 register INT_Int46Handler(word) BUILTIN_DefaultIntHandler
171 register INT_Int47Handler(word) BUILTIN_DefaultIntHandler
172 register INT_Int48Handler(word) BUILTIN_DefaultIntHandler
173 register INT_Int49Handler(word) BUILTIN_DefaultIntHandler
174 register INT_Int4aHandler(word) BUILTIN_DefaultIntHandler
175 register INT_Int4bHandler(word) INT_Int4bHandler
176 register INT_Int4cHandler(word) BUILTIN_DefaultIntHandler
177 register INT_Int4dHandler(word) BUILTIN_DefaultIntHandler
178 register INT_Int4eHandler(word) BUILTIN_DefaultIntHandler
179 register INT_Int4fHandler(word) BUILTIN_DefaultIntHandler
180 register INT_Int50Handler(word) BUILTIN_DefaultIntHandler
181 register INT_Int51Handler(word) BUILTIN_DefaultIntHandler
182 register INT_Int52Handler(word) BUILTIN_DefaultIntHandler
183 register INT_Int53Handler(word) BUILTIN_DefaultIntHandler
184 register INT_Int54Handler(word) BUILTIN_DefaultIntHandler
185 register INT_Int55Handler(word) BUILTIN_DefaultIntHandler
186 register INT_Int56Handler(word) BUILTIN_DefaultIntHandler
187 register INT_Int57Handler(word) BUILTIN_DefaultIntHandler
188 register INT_Int58Handler(word) BUILTIN_DefaultIntHandler
189 register INT_Int59Handler(word) BUILTIN_DefaultIntHandler
190 register INT_Int5aHandler(word) BUILTIN_DefaultIntHandler
191 register INT_Int5bHandler(word) BUILTIN_DefaultIntHandler
192 register INT_Int5cHandler(word) NetBIOSCall
193 register INT_Int5dHandler(word) BUILTIN_DefaultIntHandler
194 register INT_Int5eHandler(word) BUILTIN_DefaultIntHandler
195 register INT_Int5fHandler(word) BUILTIN_DefaultIntHandler
196 register INT_Int60Handler(word) BUILTIN_DefaultIntHandler
197 register INT_Int61Handler(word) BUILTIN_DefaultIntHandler
198 register INT_Int62Handler(word) BUILTIN_DefaultIntHandler
199 register INT_Int63Handler(word) BUILTIN_DefaultIntHandler
200 register INT_Int64Handler(word) BUILTIN_DefaultIntHandler
201 register INT_Int65Handler(word) BUILTIN_DefaultIntHandler
202 register INT_Int66Handler(word) BUILTIN_DefaultIntHandler
203 register INT_Int67Handler(word) BUILTIN_DefaultIntHandler
204 register INT_Int68Handler(word) BUILTIN_DefaultIntHandler
205 register INT_Int69Handler(word) BUILTIN_DefaultIntHandler
206 register INT_Int6aHandler(word) BUILTIN_DefaultIntHandler
207 register INT_Int6bHandler(word) BUILTIN_DefaultIntHandler
208 register INT_Int6cHandler(word) BUILTIN_DefaultIntHandler
209 register INT_Int6dHandler(word) BUILTIN_DefaultIntHandler
210 register INT_Int6eHandler(word) BUILTIN_DefaultIntHandler
211 register INT_Int6fHandler(word) BUILTIN_DefaultIntHandler
212 register INT_Int70Handler(word) BUILTIN_DefaultIntHandler
213 register INT_Int71Handler(word) BUILTIN_DefaultIntHandler
214 register INT_Int72Handler(word) BUILTIN_DefaultIntHandler
215 register INT_Int73Handler(word) BUILTIN_DefaultIntHandler
216 register INT_Int74Handler(word) BUILTIN_DefaultIntHandler
217 register INT_Int75Handler(word) BUILTIN_DefaultIntHandler
218 register INT_Int76Handler(word) BUILTIN_DefaultIntHandler
219 register INT_Int77Handler(word) BUILTIN_DefaultIntHandler
220 register INT_Int78Handler(word) BUILTIN_DefaultIntHandler
221 register INT_Int79Handler(word) BUILTIN_DefaultIntHandler
222 register INT_Int7aHandler(word) BUILTIN_DefaultIntHandler
223 register INT_Int7bHandler(word) BUILTIN_DefaultIntHandler
224 register INT_Int7cHandler(word) BUILTIN_DefaultIntHandler
225 register INT_Int7dHandler(word) BUILTIN_DefaultIntHandler
226 register INT_Int7eHandler(word) BUILTIN_DefaultIntHandler
227 register INT_Int7fHandler(word) BUILTIN_DefaultIntHandler
228 register INT_Int80Handler(word) BUILTIN_DefaultIntHandler
229 register INT_Int81Handler(word) BUILTIN_DefaultIntHandler
230 register INT_Int82Handler(word) BUILTIN_DefaultIntHandler
231 register INT_Int83Handler(word) BUILTIN_DefaultIntHandler
232 register INT_Int84Handler(word) BUILTIN_DefaultIntHandler
233 register INT_Int85Handler(word) BUILTIN_DefaultIntHandler
234 register INT_Int86Handler(word) BUILTIN_DefaultIntHandler
235 register INT_Int87Handler(word) BUILTIN_DefaultIntHandler
236 register INT_Int88Handler(word) BUILTIN_DefaultIntHandler
237 register INT_Int89Handler(word) BUILTIN_DefaultIntHandler
238 register INT_Int8aHandler(word) BUILTIN_DefaultIntHandler
239 register INT_Int8bHandler(word) BUILTIN_DefaultIntHandler
240 register INT_Int8cHandler(word) BUILTIN_DefaultIntHandler
241 register INT_Int8dHandler(word) BUILTIN_DefaultIntHandler
242 register INT_Int8eHandler(word) BUILTIN_DefaultIntHandler
243 register INT_Int8fHandler(word) BUILTIN_DefaultIntHandler
244 register INT_Int90Handler(word) BUILTIN_DefaultIntHandler
245 register INT_Int91Handler(word) BUILTIN_DefaultIntHandler
246 register INT_Int92Handler(word) BUILTIN_DefaultIntHandler
247 register INT_Int93Handler(word) BUILTIN_DefaultIntHandler
248 register INT_Int94Handler(word) BUILTIN_DefaultIntHandler
249 register INT_Int95Handler(word) BUILTIN_DefaultIntHandler
250 register INT_Int96Handler(word) BUILTIN_DefaultIntHandler
251 register INT_Int97Handler(word) BUILTIN_DefaultIntHandler
252 register INT_Int98Handler(word) BUILTIN_DefaultIntHandler
253 register INT_Int99Handler(word) BUILTIN_DefaultIntHandler
254 register INT_Int9aHandler(word) BUILTIN_DefaultIntHandler
255 register INT_Int9bHandler(word) BUILTIN_DefaultIntHandler
256 register INT_Int9cHandler(word) BUILTIN_DefaultIntHandler
257 register INT_Int9dHandler(word) BUILTIN_DefaultIntHandler
258 register INT_Int9eHandler(word) BUILTIN_DefaultIntHandler
259 register INT_Int9fHandler(word) BUILTIN_DefaultIntHandler
260 register INT_Inta0Handler(word) BUILTIN_DefaultIntHandler
261 register INT_Inta1Handler(word) BUILTIN_DefaultIntHandler
262 register INT_Inta2Handler(word) BUILTIN_DefaultIntHandler
263 register INT_Inta3Handler(word) BUILTIN_DefaultIntHandler
264 register INT_Inta4Handler(word) BUILTIN_DefaultIntHandler
265 register INT_Inta5Handler(word) BUILTIN_DefaultIntHandler
266 register INT_Inta6Handler(word) BUILTIN_DefaultIntHandler
267 register INT_Inta7Handler(word) BUILTIN_DefaultIntHandler
268 register INT_Inta8Handler(word) BUILTIN_DefaultIntHandler
269 register INT_Inta9Handler(word) BUILTIN_DefaultIntHandler
270 register INT_IntaaHandler(word) BUILTIN_DefaultIntHandler
271 register INT_IntabHandler(word) BUILTIN_DefaultIntHandler
272 register INT_IntacHandler(word) BUILTIN_DefaultIntHandler
273 register INT_IntadHandler(word) BUILTIN_DefaultIntHandler
274 register INT_IntaeHandler(word) BUILTIN_DefaultIntHandler
275 register INT_IntafHandler(word) BUILTIN_DefaultIntHandler
276 register INT_Intb0Handler(word) BUILTIN_DefaultIntHandler
277 register INT_Intb1Handler(word) BUILTIN_DefaultIntHandler
278 register INT_Intb2Handler(word) BUILTIN_DefaultIntHandler
279 register INT_Intb3Handler(word) BUILTIN_DefaultIntHandler
280 register INT_Intb4Handler(word) BUILTIN_DefaultIntHandler
281 register INT_Intb5Handler(word) BUILTIN_DefaultIntHandler
282 register INT_Intb6Handler(word) BUILTIN_DefaultIntHandler
283 register INT_Intb7Handler(word) BUILTIN_DefaultIntHandler
284 register INT_Intb8Handler(word) BUILTIN_DefaultIntHandler
285 register INT_Intb9Handler(word) BUILTIN_DefaultIntHandler
286 register INT_IntbaHandler(word) BUILTIN_DefaultIntHandler
287 register INT_IntbbHandler(word) BUILTIN_DefaultIntHandler
288 register INT_IntbcHandler(word) BUILTIN_DefaultIntHandler
289 register INT_IntbdHandler(word) BUILTIN_DefaultIntHandler
290 register INT_IntbeHandler(word) BUILTIN_DefaultIntHandler
291 register INT_IntbfHandler(word) BUILTIN_DefaultIntHandler
292 register INT_Intc0Handler(word) BUILTIN_DefaultIntHandler
293 register INT_Intc1Handler(word) BUILTIN_DefaultIntHandler
294 register INT_Intc2Handler(word) BUILTIN_DefaultIntHandler
295 register INT_Intc3Handler(word) BUILTIN_DefaultIntHandler
296 register INT_Intc4Handler(word) BUILTIN_DefaultIntHandler
297 register INT_Intc5Handler(word) BUILTIN_DefaultIntHandler
298 register INT_Intc6Handler(word) BUILTIN_DefaultIntHandler
299 register INT_Intc7Handler(word) BUILTIN_DefaultIntHandler
300 register INT_Intc8Handler(word) BUILTIN_DefaultIntHandler
301 register INT_Intc9Handler(word) BUILTIN_DefaultIntHandler
302 register INT_IntcaHandler(word) BUILTIN_DefaultIntHandler
303 register INT_IntcbHandler(word) BUILTIN_DefaultIntHandler
304 register INT_IntccHandler(word) BUILTIN_DefaultIntHandler
305 register INT_IntcdHandler(word) BUILTIN_DefaultIntHandler
306 register INT_IntceHandler(word) BUILTIN_DefaultIntHandler
307 register INT_IntcfHandler(word) BUILTIN_DefaultIntHandler
308 register INT_Intd0Handler(word) BUILTIN_DefaultIntHandler
309 register INT_Intd1Handler(word) BUILTIN_DefaultIntHandler
310 register INT_Intd2Handler(word) BUILTIN_DefaultIntHandler
311 register INT_Intd3Handler(word) BUILTIN_DefaultIntHandler
312 register INT_Intd4Handler(word) BUILTIN_DefaultIntHandler
313 register INT_Intd5Handler(word) BUILTIN_DefaultIntHandler
314 register INT_Intd6Handler(word) BUILTIN_DefaultIntHandler
315 register INT_Intd7Handler(word) BUILTIN_DefaultIntHandler
316 register INT_Intd8Handler(word) BUILTIN_DefaultIntHandler
317 register INT_Intd9Handler(word) BUILTIN_DefaultIntHandler
318 register INT_IntdaHandler(word) BUILTIN_DefaultIntHandler
319 register INT_IntdbHandler(word) BUILTIN_DefaultIntHandler
320 register INT_IntdcHandler(word) BUILTIN_DefaultIntHandler
321 register INT_IntddHandler(word) BUILTIN_DefaultIntHandler
322 register INT_IntdeHandler(word) BUILTIN_DefaultIntHandler
323 register INT_IntdfHandler(word) BUILTIN_DefaultIntHandler
324 register INT_Inte0Handler(word) BUILTIN_DefaultIntHandler
325 register INT_Inte1Handler(word) BUILTIN_DefaultIntHandler
326 register INT_Inte2Handler(word) BUILTIN_DefaultIntHandler
327 register INT_Inte3Handler(word) BUILTIN_DefaultIntHandler
328 register INT_Inte4Handler(word) BUILTIN_DefaultIntHandler
329 register INT_Inte5Handler(word) BUILTIN_DefaultIntHandler
330 register INT_Inte6Handler(word) BUILTIN_DefaultIntHandler
331 register INT_Inte7Handler(word) BUILTIN_DefaultIntHandler
332 register INT_Inte8Handler(word) BUILTIN_DefaultIntHandler
333 register INT_Inte9Handler(word) BUILTIN_DefaultIntHandler
334 register INT_InteaHandler(word) BUILTIN_DefaultIntHandler
335 register INT_IntebHandler(word) BUILTIN_DefaultIntHandler
336 register INT_IntecHandler(word) BUILTIN_DefaultIntHandler
337 register INT_IntedHandler(word) BUILTIN_DefaultIntHandler
338 register INT_InteeHandler(word) BUILTIN_DefaultIntHandler
339 register INT_IntefHandler(word) BUILTIN_DefaultIntHandler
340 register INT_Intf0Handler(word) BUILTIN_DefaultIntHandler
341 register INT_Intf1Handler(word) BUILTIN_DefaultIntHandler
342 register INT_Intf2Handler(word) BUILTIN_DefaultIntHandler
343 register INT_Intf3Handler(word) BUILTIN_DefaultIntHandler
344 register INT_Intf4Handler(word) BUILTIN_DefaultIntHandler
345 register INT_Intf5Handler(word) BUILTIN_DefaultIntHandler
346 register INT_Intf6Handler(word) BUILTIN_DefaultIntHandler
347 register INT_Intf7Handler(word) BUILTIN_DefaultIntHandler
348 register INT_Intf8Handler(word) BUILTIN_DefaultIntHandler
349 register INT_Intf9Handler(word) BUILTIN_DefaultIntHandler
350 register INT_IntfaHandler(word) BUILTIN_DefaultIntHandler
351 register INT_IntfbHandler(word) BUILTIN_DefaultIntHandler
352 register INT_IntfcHandler(word) BUILTIN_DefaultIntHandler
353 register INT_IntfdHandler(word) BUILTIN_DefaultIntHandler
354 register INT_IntfeHandler(word) BUILTIN_DefaultIntHandler
355 register INT_IntffHandler(word) BUILTIN_DefaultIntHandler

# VxDs. The first Vxd is at 400
#
#400+VXD_ID register <VxD handler>() <VxD handler>
#
405 register VXD_Timer() VXD_Timer
414 register VXD_Comm() VXD_Comm
#415 register VXD_Printer() VXD_Printer
423 register VXD_Shell() VXD_Shell
433 register VXD_PageFile() VXD_PageFile
