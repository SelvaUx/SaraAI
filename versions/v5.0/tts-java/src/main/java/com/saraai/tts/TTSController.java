package com.saraai.tts;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/tts")
public class TTSController {

    private final TTSService ttsService;

    @Autowired
    public TTSController(TTSService ttsService) {
        this.ttsService = ttsService;
    }

    @PostMapping("/speak")
    public void speak(@RequestBody String text) {
        ttsService.speak(text);
    }
}
