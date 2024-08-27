# Reference
<details><summary><code>client.<a href="src/vocode/client.py">metrics_metrics_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint that serves Prometheus metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.metrics_metrics_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## numbers
<details><summary><code>client.numbers.<a href="src/vocode/numbers/client.py">list_numbers</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.numbers.list_numbers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.numbers.<a href="src/vocode/numbers/client.py">get_number</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.numbers.get_number(
    phone_number="phone_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.numbers.<a href="src/vocode/numbers/client.py">buy_number</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.numbers.buy_number()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**area_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**telephony_provider:** `typing.Optional[BuyPhoneNumberRequestTelephonyProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**telephony_account_connection:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**inbound_agent:** `typing.Optional[BuyPhoneNumberRequestInboundAgent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.numbers.<a href="src/vocode/numbers/client.py">update_number</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.numbers.update_number(
    phone_number="phone_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**outbound_only:** `typing.Optional[UpdateNumberRequestOutboundOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**example_context:** `typing.Optional[UpdateNumberRequestExampleContext]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[UpdateNumberRequestLabel]` 
    
</dd>
</dl>

<dl>
<dd>

**inbound_agent:** `typing.Optional[UpdateNumberRequestInboundAgent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.numbers.<a href="src/vocode/numbers/client.py">cancel_number</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.numbers.cancel_number(
    phone_number="phone_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.numbers.<a href="src/vocode/numbers/client.py">link_number</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.numbers.link_number(
    phone_number="phone_number",
    telephony_account_connection="telephony_account_connection",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**telephony_account_connection:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**outbound_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**inbound_agent:** `typing.Optional[LinkPhoneNumberRequestInboundAgent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## calls
<details><summary><code>client.calls.<a href="src/vocode/calls/client.py">list_calls</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.calls.list_calls()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vocode/calls/client.py">get_call</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.calls.get_call(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vocode/calls/client.py">end_call</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.calls.end_call(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vocode/calls/client.py">create_call</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.calls.create_call(
    from_number="from_number",
    to_number="to_number",
    agent="agent",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent:** `CreateCallRequestAgent` 
    
</dd>
</dl>

<dl>
<dd>

**on_no_human_answer:** `typing.Optional[CreateCallRequestOnNoHumanAnswer]` 
    
</dd>
</dl>

<dl>
<dd>

**run_do_not_call_detection:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hipaa_compliant:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**telephony_params:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vocode/calls/client.py">get_recording</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.calls.get_recording(
    id="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usage
<details><summary><code>client.usage.<a href="src/vocode/usage/client.py">get_usage</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.usage.get_usage()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions
<details><summary><code>client.actions.<a href="src/vocode/actions/client.py">get_action</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.actions.get_action(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/vocode/actions/client.py">list_actions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.actions.list_actions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/vocode/actions/client.py">create_action</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import AddToConferenceActionParams, AddToConferenceConfig, Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.actions.create_action(
    request=AddToConferenceActionParams(
        config=AddToConferenceConfig(
            phone_number="phone_number",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ActionParamsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/vocode/actions/client.py">update_action</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import AddToConferenceActionUpdateParams, Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.actions.update_action(
    id="id",
    request=AddToConferenceActionUpdateParams(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ActionUpdateParamsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents
<details><summary><code>client.agents.<a href="src/vocode/agents/client.py">get_agent</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.agents.get_agent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/vocode/agents/client.py">list_agents</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.agents.list_agents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/vocode/agents/client.py">create_agent</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.agents.create_agent(
    prompt="prompt",
    voice="voice",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `AgentParamsPrompt` 
    
</dd>
</dl>

<dl>
<dd>

**voice:** `AgentParamsVoice` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[Language]` 
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[AgentParamsActionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_message:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[AgentParamsWebhook]` 
    
</dd>
</dl>

<dl>
<dd>

**vector_database:** `typing.Optional[AgentParamsVectorDatabase]` 
    
</dd>
</dl>

<dl>
<dd>

**interrupt_sensitivity:** `typing.Optional[InterruptSensitivity]` 
    
</dd>
</dl>

<dl>
<dd>

**context_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**noise_suppression:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**endpointing_sensitivity:** `typing.Optional[AgentParamsEndpointingSensitivity]` 
    
</dd>
</dl>

<dl>
<dd>

**ivr_navigation_mode:** `typing.Optional[AgentParamsIvrNavigationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_speed:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_message_delay:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_model_name_override:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ask_if_human_present_on_idle:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_account_connection:** `typing.Optional[AgentParamsOpenaiAccountConnection]` 
    
</dd>
</dl>

<dl>
<dd>

**run_do_not_call_detection:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_fallback:** `typing.Optional[InternalLlmFallback]` 
    
</dd>
</dl>

<dl>
<dd>

**deepgram_keywords:** `typing.Optional[
    typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**idle_time_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/vocode/agents/client.py">update_agent</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.agents.update_agent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[AgentUpdateParamsName]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[AgentUpdateParamsPrompt]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[AgentUpdateParamsLanguage]` 
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[AgentUpdateParamsActions]` 
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[AgentUpdateParamsVoice]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_message:** `typing.Optional[AgentUpdateParamsInitialMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[AgentUpdateParamsWebhook]` 
    
</dd>
</dl>

<dl>
<dd>

**vector_database:** `typing.Optional[AgentUpdateParamsVectorDatabase]` 
    
</dd>
</dl>

<dl>
<dd>

**interrupt_sensitivity:** `typing.Optional[AgentUpdateParamsInterruptSensitivity]` 
    
</dd>
</dl>

<dl>
<dd>

**context_endpoint:** `typing.Optional[AgentUpdateParamsContextEndpoint]` 
    
</dd>
</dl>

<dl>
<dd>

**noise_suppression:** `typing.Optional[AgentUpdateParamsNoiseSuppression]` 
    
</dd>
</dl>

<dl>
<dd>

**endpointing_sensitivity:** `typing.Optional[AgentUpdateParamsEndpointingSensitivity]` 
    
</dd>
</dl>

<dl>
<dd>

**ivr_navigation_mode:** `typing.Optional[AgentUpdateParamsIvrNavigationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_speed:** `typing.Optional[AgentUpdateParamsConversationSpeed]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_message_delay:** `typing.Optional[AgentUpdateParamsInitialMessageDelay]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_model_name_override:** `typing.Optional[AgentUpdateParamsOpenaiModelNameOverride]` 
    
</dd>
</dl>

<dl>
<dd>

**ask_if_human_present_on_idle:** `typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle]` 
    
</dd>
</dl>

<dl>
<dd>

**openai_account_connection:** `typing.Optional[AgentUpdateParamsOpenaiAccountConnection]` 
    
</dd>
</dl>

<dl>
<dd>

**run_do_not_call_detection:** `typing.Optional[AgentUpdateParamsRunDoNotCallDetection]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_fallback:** `typing.Optional[AgentUpdateParamsLlmFallback]` 
    
</dd>
</dl>

<dl>
<dd>

**deepgram_keywords:** `typing.Optional[AgentUpdateParamsDeepgramKeywords]` 
    
</dd>
</dl>

<dl>
<dd>

**idle_time_seconds:** `typing.Optional[AgentUpdateParamsIdleTimeSeconds]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Voices
<details><summary><code>client.voices.<a href="src/vocode/voices/client.py">get_voice</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.voices.get_voice(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.voices.<a href="src/vocode/voices/client.py">list_voices</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.voices.list_voices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.voices.<a href="src/vocode/voices/client.py">create_voice</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import AzureVoiceParams, Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.voices.create_voice(
    request=AzureVoiceParams(
        voice_name="voice_name",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `VoiceParamsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.voices.<a href="src/vocode/voices/client.py">update_voice</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import AzureVoiceUpdateParams, Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.voices.update_voice(
    id="id",
    request=AzureVoiceUpdateParams(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `VoiceUpdateParamsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/vocode/webhooks/client.py">get_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.webhooks.get_webhook(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/vocode/webhooks/client.py">list_webhooks</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.webhooks.list_webhooks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/vocode/webhooks/client.py">create_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.webhooks.create_webhook(
    subscriptions=["event_message"],
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscriptions:** `typing.Sequence[EventType]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[HttpMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/vocode/webhooks/client.py">update_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.webhooks.update_webhook(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subscriptions:** `typing.Optional[WebhookUpdateParamsSubscriptions]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[WebhookUpdateParamsUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[WebhookUpdateParamsMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts
<details><summary><code>client.prompts.<a href="src/vocode/prompts/client.py">get_prompt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.prompts.get_prompt(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/vocode/prompts/client.py">list_prompts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.prompts.list_prompts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/vocode/prompts/client.py">create_prompt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.prompts.create_prompt()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collect_fields:** `typing.Optional[typing.Sequence[CollectField]]` 
    
</dd>
</dl>

<dl>
<dd>

**context_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[PromptParamsPromptTemplate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/vocode/prompts/client.py">update_prompt</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.prompts.update_prompt(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[PromptUpdateParamsContent]` 
    
</dd>
</dl>

<dl>
<dd>

**collect_fields:** `typing.Optional[PromptUpdateParamsCollectFields]` 
    
</dd>
</dl>

<dl>
<dd>

**context_endpoint:** `typing.Optional[PromptUpdateParamsContextEndpoint]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[PromptUpdateParamsPromptTemplate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## VectorDatabases
<details><summary><code>client.vector_databases.<a href="src/vocode/vector_databases/client.py">get_vector_database</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.vector_databases.get_vector_database(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vector_databases.<a href="src/vocode/vector_databases/client.py">list_vector_databases</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.vector_databases.list_vector_databases()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vector_databases.<a href="src/vocode/vector_databases/client.py">create_vector_database</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.vector_databases.create_vector_database(
    index="index",
    api_key="api_key",
    api_environment="api_environment",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**index:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**api_environment:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vector_databases.<a href="src/vocode/vector_databases/client.py">update_vector_database</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.vector_databases.update_vector_database(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**index:** `typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]` 
    
</dd>
</dl>

<dl>
<dd>

**api_environment:** `typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AccountConnections
<details><summary><code>client.account_connections.<a href="src/vocode/account_connections/client.py">get_account_connection</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.account_connections.get_account_connection(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_connections.<a href="src/vocode/account_connections/client.py">list_account_connections</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.account_connections.list_account_connections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_column:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_connections.<a href="src/vocode/account_connections/client.py">create_account_connection</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import OpenAiAccountConnectionParams, OpenAiCredentials, Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.account_connections.create_account_connection(
    request=OpenAiAccountConnectionParams(
        credentials=OpenAiCredentials(
            openai_api_key="openai_api_key",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AccountConnectionParamsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_connections.<a href="src/vocode/account_connections/client.py">update_account_connection</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import OpenAiAccountConnectionUpdateParams, Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.account_connections.update_account_connection(
    id="id",
    request=OpenAiAccountConnectionUpdateParams(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AccountConnectionUpdateParamsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_connections.<a href="src/vocode/account_connections/client.py">add_to_steering_pool</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.account_connections.add_to_steering_pool(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[AddToSteeringPoolBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_connections.<a href="src/vocode/account_connections/client.py">remove_from_steering_pool</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vocode import Vocode

client = Vocode(
    token="YOUR_TOKEN",
)
client.account_connections.remove_from_steering_pool(
    id="id",
    phone_number="phone_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

