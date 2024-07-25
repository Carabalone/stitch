import { AntDesign } from '@expo/vector-icons';
import React from 'react';
import { View } from 'react-native';

export function Qrcode({ isActive, color, focusedColor }) {
    const containerClass = `p-2 ${true ? 'border-2 border-blue-500 rounded-full' : ''}`;

    return (
            <View className='bg-red'>
                <AntDesign name="qrcode" size={24} color={isActive ? focusedColor : color} />
            </View>
    );
}
